import os

from flask import Flask, render_template

from .utils.utils import print_log

app = Flask(__name__, instance_relative_config=True)
ProjectDir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir))
app.basedir = ProjectDir
# print_log('Project Dir: {}'.format(ProjectDir))

# ###################
# ## Loading Configs
# ###################
# Load config from '/config.py'
if os.path.isfile('{}/config.py'.format(ProjectDir)):
    app.config.from_object('config')
    print_log('Loaded settings from "/config.py"')
else:
    print_log('Skipped loading settings from "/config.py": file not found')

# Load config from '/instance/default.py'
if (os.path.isdir('{}/instance'.format(ProjectDir)) and
        os.path.isfile('{}/instance/default.py'.format(ProjectDir))):
    app.config.from_pyfile('default.py')
    print_log('Loaded settings from "/instance/default.py"')
else:
    print_log(
        'Skipped loading settings from "/instance/default.py": file not found')

# Load config from envvar, make sense to add APP_CONFIG_FILE to env var
try:
    app.config.from_envvar('APP_CONFIG_FILE')
except:
    print_log('The environment variable is not set and skip env var settings.')

# print_log(app.config)

# #############################
# ## Enable SQLAlchemy Support
# #############################
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
dbt = SQLAlchemy(app)


# ###############################
# ## Enable Flask-Admin Support
# ###############################
from flask.ext.admin import Admin
admin = Admin(app, name='MyToken Backend', template_mode='bootstrap3')

from flask_basicauth import BasicAuth
basic_auth = BasicAuth(app)

from flask_admin.contrib.sqla import ModelView
from .models.social import Social, SocialView
from .models.currency import Currency, CurrencyView
from .models.ico import Ico, IcoView
from .models.announcement import Announcement, AnnouncementView
from .models.news import News, NewsView
from .models.market import Market, MarketView
from .models.top_market import TopMarket, TopMarketView
from .models.social_raw import SocialCurrency, SocialCurrencyView
from .models.country import Country, CountryView
from .models.ico_raw import ICORaw, ICORawView
from .models.ico_project import ICOProject, ICOProjectView
from .models.ico_project import Rater, RaterView
from .models.ico_project import Tag, TagView
# from .models.ico_project import ProjectRate, ProjectRateView

admin.add_view(AnnouncementView(Announcement, db.session, name='公告'))
admin.add_view(CurrencyView(Currency, db.session, name='数字货币'))
admin.add_view(IcoView(Ico, db.session, name='ICO信息'))
admin.add_view(SocialView(Social, db.session, name='社交／推特', category='内容'))
admin.add_view(NewsView(News, db.session, name='早知道', category='内容'))
admin.add_view(MarketView(Market, db.session, name='交易所', category='交易所'))
admin.add_view(TopMarketView(TopMarket, db.session, name='App交易所', category='交易所'))
admin.add_view(ICOProjectView(ICOProject, db.session, name='ICO项目', category='ICOPROJECT'))
admin.add_view(RaterView(Rater, db.session, name='评级者', category='ICOPROJECT'))
admin.add_view(TagView(Tag, db.session, name='标签', category='ICOPROJECT'))
# admin.add_view(ProjectRateView(ProjectRate, db.session, name='评分', category='ICOPROJECT'))
admin.add_view(CountryView(Country, db.session, name='国家', category='其他'))
admin.add_view(SocialCurrencyView(SocialCurrency, db.session, name='社交账号', category='预处理'))
admin.add_view(ICORawView(ICORaw, db.session, name='ico项目-源', category='预处理'))


# ###################
# ## Enable Markdown
# ###################
from flaskext.markdown import Markdown
Markdown(app)

# ####################
# ## Enable Blueprint
# ####################
from .views.home import home

app.register_blueprint(home)

# ########################
# ## Enable Email Support
# ########################
from flask_mail import Mail
mail = Mail(app)

# ##################
# ## Enable Bcrypt
# ##################
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# ##################
# ## Enable Toolbar
# ##################
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)


@app.before_request
def do_before_request():
    # you can put database init code here
    pass


@app.teardown_request
def do_teardown_request(exception):
    # you can put database close code here
    pass


@app.errorhandler(404)
def file_not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('error/500.html'), 500


# ###################
# ## Enable ErrorLog
# ###################
if not app.debug:
    import logging
    # we use log file to log errors here
    # you can also implement mail notification
    # see logging.handlers.SMTPHandler
    from logging.handlers import TimedRotatingFileHandler
    log_file = '{dir}/{file}'.format(dir=app.basedir,
                                     file=app.config['ERROR_LOG'])
    if not os.path.exists(os.path.split(log_file)[0]):
        os.makedirs(os.path.split(log_file)[0])
    file_handler = TimedRotatingFileHandler(log_file,
                                            when='midnight',
                                            interval=1,
                                            backupCount=0)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('Project start up...')

import os

from flask import Flask

from .utils.utils import print_log

app = Flask(__name__, instance_relative_config=True)
ProjectDir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir))
print_log('Project Dir: {}'.format(ProjectDir))

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

# Load config from envvar
app.config.from_pyfile('default.py')

# print_log(app.config)

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

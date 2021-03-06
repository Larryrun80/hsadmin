from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   flash,
                   jsonify)

from ..models.forms import SigninForm

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/api')
def api_index():
    return jsonify({
            'status': 100,
            'message': 'ok',
            'result': {
                'message': 'welcome to HSFramework'
            }
        })


@home.route('/signup')
def signup():
    pass


@home.route('/signin', methods=["GET", "POST"])
def signin():
    form = SigninForm()
    if form.validate_on_submit():

        # Check username and password here

        return redirect(url_for('home.index'))
    flash('Now no sign in logic is implemented, go /project/views/home and code it')
    return render_template('home/signin.html', form=form)

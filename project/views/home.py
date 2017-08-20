from flask import (Blueprint,
                   render_template,
                   jsonify)

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

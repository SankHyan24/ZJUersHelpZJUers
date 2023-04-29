import os

from flask import Flask,render_template
from util.mysql import get_db_info

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=get_db_info(),
    )
    
    
    
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # main page
    # @app.route('/')
    # def index():
    #     return render_template('index.html')    
   

    
    
    from flaskr.apps import auth
    from flaskr.apps import blog
    from flaskr.apps.user_system.user_route import bp as user_bp
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(user_bp)
    
    
    app.add_url_rule("/", endpoint="index")

    return app
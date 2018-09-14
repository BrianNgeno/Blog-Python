from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_simplemde import SimpleMDE


bootstrap = Bootstrap()
simplemde = SimpleMDE()


def create_app(config_name):
    app = Flask(__name__)

    '''
    creating the app configurations
    '''
    app.config.from_object(config_options[config_name])
    
     #initializing the flask extensions
    bootstrap.init_app(app)
    simplemde.init_app(app)

    #Registering the bluprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app
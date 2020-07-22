from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap
from app import views
from app import error

bootstrap = Bootstrap()

   # Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

# register a blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
# setup config
from .requests import configure_request
configure_request(app)

def create_app():
   app=Flask(__name__)
   return app

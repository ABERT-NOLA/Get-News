from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap = Bootstrap(app)
def create_app(config_name):
   app=Flask(__name__)

      # Initializing application

      # Setting up configuration
   app.config.from_object(config_options[config_name])


   # Initializing Flask Extensions
   bootstrap.init_app(app)
   # register a blueprint
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)
   # setup config
   from .requests import configure_requests
   configure_requests(app)
   return app





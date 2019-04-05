from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#instantiating extensions with app instance, can run outside of instance of create_app

#db object
db = SQLAlchemy()

#cross origin request, allow api requests to server
cors = CORS()

#create flask app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    #registering extensions with app
    db.init_app(app)
    cors.init_app(app)

def register_blueprints(app):
    #registering blueprints with app instance
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')




import os

from flask import Flask
from anotherme.apis.v1 import api_v1
from anotherme.settings import config, basedir

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('anotherme')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_template_context(app)
    return app

def register_extensions(app):
    pass

def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(api_v1, subdomain='api', url_prefix='/v1')

def register_commands(app):
    pass

def register_errors(app):
    pass

def register_template_context(app):
    pass
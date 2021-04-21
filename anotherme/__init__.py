import os
import click
from flask import Flask
from anotherme.apis.v1 import api_v1
from anotherme.settings import config, basedir
from anotherme.extensions import db, login_manager, csrf
from anotherme.blueprints.auth import auth_bp



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
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    csrf.exempt(api_v1)


def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(api_v1, subdomain='api', url_prefix='/v1')
    app.register_blueprint(auth_bp)

def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

def register_errors(app):
    pass

def register_template_context(app):
    pass
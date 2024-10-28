from . import notes, simple_pages, categories, api, users, newnote
from flask import Flask, redirect, url_for, render_template
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager
import os

def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['NOTES_PER_PAGE'] = 4
    app.secret_key = os.getenv('SECRET_KEY')

    register_blueprints(app)
    register_extensions(app)

    return app

# Blueprints
def register_blueprints(app:Flask):
    app.register_blueprint(notes.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(categories.routes.blueprint)
    app.register_blueprint(api.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(newnote.routes.blueprint)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)
  login_manager.init_app(app)
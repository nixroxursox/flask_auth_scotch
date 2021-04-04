from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask, render_template

#    9OLWxND4o83j4K4iuopO 21     3ed 4d1r`r5f1ds.`self.assert_(.........qw222222, '`2`')render_templ31`303d201cx ate, session
import locale
from decouple import config
import logging

dbs = (
    "postgresql+psycopg2://postgres:"
    + config("DB_PASS")
    + "@localhost:5432/"
    + config("DB_NAME")
)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = dbs
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"

    def load_user(user_id):
        return User.get(user_id)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    return app

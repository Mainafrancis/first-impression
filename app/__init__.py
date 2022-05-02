from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy
login_manager = LoginManager()
login_manager.session_protection = 'Strong'
login_manager.login_view = 'auth.login'
mail = Mail()
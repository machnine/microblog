import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask                 # import Flask class from flask module
from config import Config               # import config class from the config.py in the same folder as microblog.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)                   # app = name of the Flask instance
app.config.from_object(Config)          # read app (instance) config
db = SQLAlchemy(app)                    # database object
migrate = Migrate(app, db)              # db migration object
login = LoginManager(app)               # flask-login object
login.login_view = 'login'              # view function handles the login 

from app import routes, models, errors          # from the ..\app folder import routes.py

if not app.debug:
    # email errors to admin
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                                       fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                                       toaddrs=app.config['ADMINS'],
                                       subject='Microblog Failure',
                                       credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

    # log errors into file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
                              '%(asctime)s %(levelname)s: %(message)s'
                              ' [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

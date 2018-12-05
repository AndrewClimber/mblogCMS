# venv\Scripts\deactivate
# venv\Scripts\activate
# export FLASK_APP=microblog.py
# set FLASK_APP=microblog.py
# set FLASK_DEBUG=1

# set MAIL_SERVER=smtp.googlemail.com
# set export MAIL_PORT=587
# set MAIL_USE_TLS=1
# set MAIL_USERNAME=oradbatest@gmail.
# set MAIL_PASSWORD=Rjynhjkkth.sd34


from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#################################################
import logging
from logging.handlers import SMTPHandler
#################################################
from logging.handlers import RotatingFileHandler
import os
#################################################

mblog_app = Flask(__name__)
mblog_app.config.from_object(Config)
db = SQLAlchemy(mblog_app)
migrate = Migrate(mblog_app, db)
login = LoginManager(mblog_app)
login.login_view = 'login'

print('* mblog_app.debug =',mblog_app.debug)

if mblog_app.debug == False:
    if mblog_app.config['MAIL_SERVER']:
        auth = None
        if mblog_app.config['MAIL_USERNAME'] or mblog_app.config['MAIL_PASSWORD']:
            auth = (mblog_app.config['MAIL_USERNAME'], mblog_app.config['MAIL_PASSWORD'])
        secure = None
        if mblog_app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(mblog_app.config['MAIL_SERVER'], mblog_app.config['MAIL_PORT']),
            fromaddr='no-reply@' + mblog_app.config['MAIL_SERVER'],
            toaddrs=mblog_app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        mblog_app.logger.addHandler(mail_handler)

if  mblog_app.debug == False:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                           backupCount=10)
    file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    mblog_app.logger.addHandler(file_handler)

    mblog_app.logger.setLevel(logging.INFO)
    mblog_app.logger.info('Microblog startup')


from app import routes, models, errors

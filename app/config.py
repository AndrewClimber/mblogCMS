# -*- coding: utf-8 -*-

# Переменная конфигурации SECRET_KEY является важной частью большинства приложений Flask.
# Flask и некоторые его расширения используют значение секретного ключа в качестве
# криптографического ключа, полезного для генерации подписей или токенов.
# Расширение Flask-WTF использует его для защиты веб-форм от противной атаки под названием
# Cross-Site Request Forgery или CSRF (произносится как «seasurf»).

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Сначала пробует прочитать из переменной среды. Если не получилось, то из переменной
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
# Если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения
# объектов и посылать сигналы.
# Данная функция требует дополнительную память, и должна быть отключена если
# не используется.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# данные сервера электронной почты
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['oradbatest@gmail.com']

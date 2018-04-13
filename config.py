import os
from configparser import ConfigParser


basedir = os.path.abspath(os.path.dirname(__file__))

cfg = ConfigParser()
cfg.read(os.path.join(basedir, 'mail.ini'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = cfg.get('mail_config', 'mail_server')
    MAIL_PORT = cfg.get('mail_config', 'mail_port')
    MAIL_USE_TLS = cfg.get('mail_config', 'mail_use_tls')
    MAIL_USERNAME = cfg.get('mail_config', 'mail_username')
    MAIL_PASSWORD = cfg.get('mail_config', 'mail_password')
    FLASKY_MAIL_SUBJECT_PREFIX = cfg.get('mail_config', 'flasky_mail_subject_prefix')
    FLASKY_MAIL_SENDER = cfg.get('mail_config', 'Flasky Admin <flasky@example.com>')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopConfig
}

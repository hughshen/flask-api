class AppConfig(object):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
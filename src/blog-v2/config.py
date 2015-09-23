class Config(object):
    APP_NAME = "Awesome Blog"

    DEBUG = True
    LOG_FILE = 'debug.log'
    LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'password'
    MYSQL_DB = 'blogdb'

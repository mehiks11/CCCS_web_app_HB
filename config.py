class Config(object):
    DEBUG = False
    TESTING= False

    SECRET_KEY = '{FILL_HERE}'

    DB_NAME ="production-db"
    DB_USERNAME = "{FILL_HERE}"
    DB_PASSWORD = '{FILL_HERE}'

    SESSION_COOKIES_SECURE = True

    BASIC_AUTH_USERNAME = '{FILL_HERE}'
    BASIC_AUTH_PASSWORD= '{FILL_HERE}'

    FILE_UPLOADS = "{Fill Absolute path to CCCS logo image}"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG= True
    SESSION_COOKIES_SECURE = False

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIES_SECURE = False
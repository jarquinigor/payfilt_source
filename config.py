from decouple import config


class DevelopmentConfig():
    DEBUG = True


configuration = {
    'development': DevelopmentConfig
}


class Config(object):
    DEBUG = True
    TESTING = False

class ApiConfig(Config):
    SECRET_KEY = "secretkey"
    OPENAI_KEY = '{your Openai api}'

config = {
    'development': ApiConfig,
    'testing': ApiConfig,
    'production': ApiConfig
}

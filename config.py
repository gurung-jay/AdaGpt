
class Config(object):
    DEBUG = True
    TESTING = False

class ApiConfig(Config):
    SECRET_KEY = "secretkey"
    OPENAI_KEY = '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'

config = {
    'development': ApiConfig,
    'testing': ApiConfig,
    'production': ApiConfig
}

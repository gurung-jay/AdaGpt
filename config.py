
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

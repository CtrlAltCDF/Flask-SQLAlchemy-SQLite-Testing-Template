from dotenv import load_dotenv
from os import environ

load_dotenv()

def get(var):
    return environ[var]

class Config(object):
    TESTING = False

class ProductionConfig(Config):
    SQLALCHEMY_URL = get("SQLALCHEMY_URI")

class DevelopmentConfig(Config):
    DEBUG=True
    DATABASE_URI = "sqlite:///dev.db"

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = "sqlite:///:memory:"

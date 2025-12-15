import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_NAME = "data.db"

class ProductionConfig(Config):
    DEBUG = False

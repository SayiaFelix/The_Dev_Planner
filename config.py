import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay@localhost/planner'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgres://clgzejipippsdw:3c38c25961098576c1b5613e6b2a13346d36ce83ca755958f4a0a313c5ce9c8b@ec2-54-204-56-171.compute-1.amazonaws.com:5432/d3naead9r38pe4'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'The Dev Planner ::'
    SENDER_EMAIL = 'sayia.lucas@student.moringaschool.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
     uri = os.getenv("DATABASE_URL")  
     if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

        SQLALCHEMY_DATABASE_URI=uri
  
  
class TestConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay@localhost/devhub_test'
  

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay@localhost/planner'
 
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

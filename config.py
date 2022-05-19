import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay@localhost/planner'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

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
    #  uri = os.getenv("DATABASE_URL")  
    #  if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://", 1)

    #     SQLALCHEMY_DATABASE_URI=uri
  
  pass
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

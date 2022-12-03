from dotenv import dotenv_values
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigClass(object):

    SECRET_KEY = "a_very_big_secret_that_must_be_longer_to_prevent_someone_from_warning"

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning
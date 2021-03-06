import os

#base directory of current file
base_directory = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.join(base_directory, 'app.db'))
    
    #added to avoid a warning in the console
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
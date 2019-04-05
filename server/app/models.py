from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    #set tablename to lowercase user for consistency
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, default=None)
    password_hash = db.Column(db.String(100), default=None)

    def create_password_hash(self, password):
        #generate a password hash for a user, only called one time
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def check_if_password_matches(self, password):
        #check if inputed password is true
        return check_password_hash(self.password, password)

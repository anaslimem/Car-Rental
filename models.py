from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(UserMixin):
    def __init__(self, **kwargs):
        self.id = kwargs.get('_id')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_username(self):
        return self.username

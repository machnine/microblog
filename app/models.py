from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts  = db.relationship('Post', backref='author', lazy='dynamic')   

    def __repr__(self):
        return f'<User {self.username}>'
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #pass the function datetime.utcnow()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))               #'user' = name of ref table, 'User' class auto-converted to lower case
    
    def __repr__(self):
        return f'<Post {self.body}>'
        

@login.user_loader
def load_user(id):
    return User.query.get(int(id))    
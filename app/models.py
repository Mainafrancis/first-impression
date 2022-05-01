from sqlalchemy.orm import backref
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    content = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = "dynamic")

    def __repr__(self):
        return f'Pitch {self.title}'


    def __init__(self,user_id, title,category,content,date_created,upvotes = 0,downvotes = 0):
        self.user_id = user_id
        self.title = title
        self.category = category
        self.content = content
        self.date_created = date_created
        self.upvotes = upvotes
        self.downvotes = downvotes

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        
        return pitches

    @classmethod
    def get_selected_pitches(cls,id):
        selected_pitches = Pitch.query.filter_by(id = id).first()

        return selected_pitches
    
    @classmethod
    def get_user_pitches(cls,id):
        user_pitches = Pitch.query.filter_by(user_id = id).all()

        return user_pitches


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, index = True)
    email = db.Column(db.String, unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    pitches = db.relationship('Pitch', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

    def get_id(self):
           return (self.user_id)

    @property
    def password(self):
        raise AttributeError('You cannot raise the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)


    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    comment_content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'Comment {self.title}'

    def get_id(self):
           return (self.comment_id)

    def __init__(self,user_id,pitch_id, title, comment_content):
        self.user_id = user_id
        self.pitch_id = pitch_id
        self.title = title
        self.comment_content = comment_content

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id = id).all()
        
        return comments

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
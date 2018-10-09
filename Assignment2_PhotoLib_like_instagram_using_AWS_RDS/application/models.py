#Name : Virti Bipin Sanghavi
#Student Id : 1001504428
#Assignment 2 - CSE 6331 Cloud Computing
#Reference to the code used from some online blogs, websites and repositories
from application import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), index=True, unique=False)
    #images =db.relationship('Images',backref='user',lazy='dynamic')

    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return '<Data %r>' % self.user_name


class Images(db.Model):
    img_id = db.Column(db.Integer, primary_key=True)
    #user_id=db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    img_url = db.Column(db.String(256), index=True, unique=False)
    title = db.Column(db.String(128), index=True, unique=False)
    likes = db.Column(db.Integer, index=True, unique=False)
    stars = db.Column(db.Integer, index=True, unique=False)
    timestamp = db.Column(db.String(256), index=True, unique=False)

class UserAccess(db.Model):
        user_id = db.Column(db.Integer, primary_key=True)
        # user_id=db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
        max_picture = db.Column(db.String(256), index=True, unique=False)
        max_size = db.Column(db.String(128), index=True, unique=False)




    def __init__(self, img_url, title,likes,stars,timestamp):
        self.img_url = img_url
        self.title = title
        self.likes=likes
        self.stars=stars
        self.timestamp=timestamp

    def __repr__(self):
        return '<Data %r>' % self.img_id
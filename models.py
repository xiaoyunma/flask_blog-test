#encoding:utf-8

from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    telephone = db.Column(db.String(11),nullable = False)
    username = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(100),nullable = False)

class Posts(db.Model):
    __tablename__ = 'posts'
    postsid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    postsauthor = db.Column(db.String(20),nullable=False)
    poststitle = db.Column(db.String(50),nullable=False)
    postscontent = db.Column(db.String(1000),nullable=False)
    poststime = db.Column(db.String(20),nullable=True)
    postsstatus = db.Column(db.String(20),nullable=True)
    postsimage = db.Column(db.String(255),nullable=True)


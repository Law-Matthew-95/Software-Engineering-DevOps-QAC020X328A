from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Ticket table
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    subject = db.Column(db.String(1000000)) # ticket subject
    description = db.Column(db.String(1000000)) # ticket description
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key
    status = db.Column(db.String(1000000)) # status of the ticket
    requester = db.Column(db.String(1000000)) # requester of the ticket

# User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key
    email = db.Column(db.String(150), unique=True) # unique email
    password = db.Column(db.String(150)) # password
    first_name = db.Column(db.String(150)) # first name
    last_name = db.Column(db.String(150)) # last name
    tickets = db.relationship('Ticket') # relationship with Ticket table
    isAdmin = db.Column(db.Boolean) # admin or not
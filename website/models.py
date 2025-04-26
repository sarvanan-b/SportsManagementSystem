from . import db 
from flask_login import UserMixin


class Register(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Event(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    reg_no = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    semester = db.Column(db.String(10), nullable=False)
    event1 = db.Column(db.String(50), nullable=False)
    event2 = db.Column(db.String(50), nullable=False)
    event3 = db.Column(db.String(50), nullable=False)


class EventDetails(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournament_name = db.Column(db.String(255), nullable=False)
    sport_name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    venue_date = db.Column(db.Date, nullable=False)
    venue = db.Column(db.String(255), nullable=False)


class ContactForm(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)


class Result(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_name = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    
    result = db.Column(db.String(50), nullable=False)
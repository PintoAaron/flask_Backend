from email.policy import default
from db import db
from datetime import datetime


class user(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100) ,nullable=False, unique = True)
    country = db.Column(db.String(100))
    date_joined = db.Column(db.Datetime , default = datetime.utcnow)
    blog_points = db.Column(db.Integer, default = 0)
    
    
    
    def __init__(self,id,firstname,lastname,password,email,country,date_joined,blog_points):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.country = country 
        self.date_joined = date_joined
        self.blog_points = blog_points
        
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    
    def serializable(self):
        return{
            
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "password":self.password,
            "email":self.email,
            "country":self.country,
            "date_joined":self.date_joined,
            "blog_points": self.blog_points
        
        }
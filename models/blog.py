from email.policy import default
from turtle import pos

from colorama import reinit
from db import db 
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class Post(db.Model):
    __tablename__ = 'Post'
    
    user_id = db.Column(db.Integer)
    post_id = db.Column(UUID(as_uuid=True), primary_key= True, unique = True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    post_date = db.Column(db.DateTime, default = datetime.utcnow)
    total_votes = db.Column(db.Integer,default = 0)
    total_comments = db.Column(db.Integer, default = 0)
    
    
    def __init__(self,user_id,post_id,title,content,post_date,total_votes,total_comments):
        self.user_id = user_id
        self.post_id = post_id
        self.title = title
        self.content = content
        self.post_date = post_date
        self.total_comments = total_comments
        self.total_votes = total_votes
        
    
    def __repr__(self):
        return 'id {}'.format(self.post_id)
    
    
    def serializable(self):
        return{
            "user_id":self.user_id,
            "post_id":self.post_id,
            "title":self.title,
            "content":self.content,
            "post_date":self.post_date,
            "total_votes":self.total_votes,
            "total_comments":self.total_comments
        }
        
class Comment(db.Model):
    __tablename__ = 'comment'
    
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.String())
    content = db.Column(db.String())
    comment_id = db.Column(UUID(as_uuid=True), primary_key= True, unique = True)
    comment_date = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __init__(self,user_id,post_id,content,comment_date,comment_id):
        self.user_id = user_id
        self.post_id = post_id
        self.comment_id = comment_id
        self.content = content
        self.comment_date = comment_date
        
    def __repr__(self):
        return 'id {}'.format(self.comment_id)
    
    
    def serializable(self):
        return{
            "user_id":self.user_id,
            "post_id":self.post_id,
            "comment_id":str(self.comment_id),
            "content":self.content,
            "comment_date":self.comment_date
            
            
        }
        
class Vote(db.Model):
    __tablename__ = 'vote'
    
    user_id = db.Column(db.String())
    post_id = db.Column(db.String())
    vote_cast = db.Column(db.String())
    
    def __init__(self,user_id,post_id,vote_cast):
        self.user_id = user_id
        self.post_id = post_id
        self.vote_cast = vote_cast
        
    
    def __repr__(self):
        return 'id {}'.format(self.post_id)
    
    
    
    def serializable(self):
        return{
            "user_id":self.user_id,
            "post_id":self.post_id,
            "vote_cast":self.user_id
        }
    
    

            

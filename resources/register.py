from flask import request
from models.user import User
from flask_restful import Resource
from db import db

class Register(Resource):
    def get(self):
        All_User = [user.serializable for user in User.query.all()]
        return{"message":"Success","data":All_User}, 200
    
    
    
    def post(self):
        json_data = request.get_data(force = True)
        if not json_data:
            return {
                "message": "No input provided"
            },400
            
            
        
        user =  User.query.filter_by(email = json_data['email']).first()
        if user:
            return{
                "message": "This email account is already registered, Please use a different email"
            }
            
        
        
        user = User(firstname=json_data['firstname'],
                    lastname=json_data['lastname'],
                    password=json_data['password'],
                    email=['email'],
                    country=json_data['country']
                    )
        
        
        db.session.add(user)
        db.session.commit()
        
        return {"message": "user Successfully registerded","data": user.serializable()}
        
        




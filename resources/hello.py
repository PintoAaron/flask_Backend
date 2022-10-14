from flask_restful import Resource


class Hello(Resource):
    def __init__(self):
        pass 
    
    def get(Self):
        return {
            "message": "WELCOME DUDE, LETS BUILD  THIS TOGETHER"
        }
        
class HelloUser(Resource):
    def __init__(self):
        pass 
    
    
    def get(self,name):
        return {
            "message": f" WELCOME {name}, LETS DO THIS"
        }
        
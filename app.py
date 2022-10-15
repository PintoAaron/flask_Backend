from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.hello import Hello,HelloUser
from db import db 
import config

app=Flask(__name__)

app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

api = Api(app)
api.add_resource(Hello,'/')
api.add_resource(HelloUser,'/<string:name>')







if __name__ == '__main__':
    app.run(debug=True)
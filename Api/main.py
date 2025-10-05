from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from extensions import database
from models import User, Game

# Set app
app = Flask(__name__)
api = Api(app)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app)

class tmp(Resource):
    def get(self):
        print("Hello")
        return

api.add_resource(tmp, '/hello')

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run("0.0.0.0", 9000, debug=True)
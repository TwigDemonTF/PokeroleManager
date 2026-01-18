# Api/routes/Auth.py

from flask_restful import Resource
from flask import request

from Api.services.AuthService import (
    register_user,
    master_login,
    player_login
)


class Register(Resource):
    def post(self):
        data = request.form if request.form else request.json
        result = register_user(
            data.get("username"),
            data.get("password")
        )
        return result, result["status"]


class MasterLogin(Resource):
    def post(self):
        data = request.form if request.form else request.json
        result = master_login(
            data.get("username"),
            data.get("password")
        )
        return result, result["status"]


class PlayerLogin(Resource):
    def post(self):
        data = request.form if request.form else request.json
        result = player_login(
            data.get("gameId"),
            data.get("gameColor")
        )
        return result, result["status"]

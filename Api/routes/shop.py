from flask import request
from flask_restful import Resource

from Api.services.ShopService import toggle_shop, get_shop_state


class ShopApi(Resource):
    def post(self):
        gameId = request.get_json().get("gameId")
        is_open = toggle_shop(gameId)

        return {
            "status": 200,
            "shopActive": is_open
        }, 200

    def get(self, gameId):
        data = get_shop_state(gameId)
        return {
            "status": 200,
            **data
        }, 200

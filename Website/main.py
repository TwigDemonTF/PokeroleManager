from flask import Flask, render_template, request, redirect, session, jsonify
from .config import DevelopmentConfig

import requests
import csv
import os
import random

app = Flask(__name__)
app.secret_key = "Fuck_You_Sessions"
app.config.from_object(DevelopmentConfig)

def contextExample():
    context = {
        "data": "banana",
    }
    return render_template('ayayay.html', **context)

@app.route('/Team', methods=['GET'])
def Team():
    context = {
        "gameId": session.get("gameId"),
        "baseUrl": app.config["BASE_URL"]
    }
    return render_template('team.html', **context)

@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usernameOrGameId = request.form.get('usernameOrGameId')
        passwordOrGameColor = request.form.get('passwordOrGameColor')
        if not request.form.get("player"):
            data = {
                "username": usernameOrGameId,
                "password": passwordOrGameColor
            }

            res = requests.post(f"{app.config["BASE_URL"]}/masterLogin", json=data)
            res = res.json()

            if res["status"] == 401:
                return render_template('login.html', message=res.get("message", "No Message Recieved"))

            # If login was successful, store user_id in session
            if "userId" in res:
                session["userId"] = res["userId"]
            if "gameId" in res:
                session["gameId"] = res["gameId"]
            print(session.get("userId"))
            print(session.get("gameId"))

            return redirect('/Game')
        else:
            passwordOrGameColor = passwordOrGameColor.title()
            data = {
                "gameId": usernameOrGameId,
                "gameColor": passwordOrGameColor,
            }

            res = requests.post(f"{app.config["BASE_URL"]}/playerLogin", json=data)
            res = res.json()
            print(res["message"])
            if res["status"] == 401:
                return render_template('login.html', message=res.get("message", "No Message Recieved"))
            
            if "gameId" in res:
                session["gameId"] = res["gameId"]
            if "gameColor" in res:
                session["gameColor"] = res["gameColor"]
            if "playerGuid" in res:
                session["playerGuid"] = res["playerGuid"]
            if "ExperiencePoints" in res:
                session["ExperiencePoints"] = res["ExperiencePoints"]
            if "Apples" in res:
                session["Apples"] = res["Apples"]

            return redirect("/Player")

    # GET request
    return render_template('login.html')

@app.route('/Register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        data = {
            "username": username,
            "password": password
        }

        res = requests.post(f"{app.config["BASE_URL"]}/register", json=data)
        res = res.json()
        return redirect('/Login')
    return render_template('register.html')

@app.route("/Logout")
def logout():
    session.clear()
    return redirect("/Login")

@app.route('/')
def addPokemon():
    context = {
        "gameId": session.get("gameId"),
        "baseUrl": app.config["BASE_URL"]
    }
    return render_template('add_pokemon.html', **context)

@app.route('/Game')
def game():
    context = {
        "gameId": session.get("gameId"),
        "baseUrl": app.config["BASE_URL"]
    }
    return render_template('game.html', **context)

@app.route("/Player")
def player():
    print(session.get("playerGuid"))
    if session.get("playerGuid"):
        return render_template("player.html", gameId=session.get("gameId"), pokemonGuid=session.get("playerGuid"), baseUrl=app.config["BASE_URL"])

@app.route("/ItemShop")
def itemShop():
    res = requests.get(f"{app.config['BASE_URL']}/Item")
    res.raise_for_status()  # optional but strongly recommended

    data = res.json()

    items = [
        item for item in data
        if item["id"] is not None
    ]

    shopStatus = requests.get(f"{app.config['BASE_URL']}/Shop/{session.get("gameId")}")
    shopStatus = shopStatus.json()

    context = {
        "items": items,
        "playerGuid": session.get("playerGuid"),
        "gameId": session.get("gameId"),
        "baseUrl": app.config["BASE_URL"],
        "shopStatus": shopStatus,
        "shopMapping": SHOP_TIER_MAPPING
    }

    return render_template("item_shop.html", **context)

def load_items(file_path):
    items = []
    weights = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue
                item_id, name, weight = row
                try:
                    weight = float(weight)
                    if 0.1 <= weight <= 1:
                        items.append((int(item_id), name))
                        weights.append(weight)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Item file not found!")
    return items, weights

@app.route("/genLootItem", methods=["GET"])
def gen_item():
    file_path = os.path.join(os.path.dirname(__file__), 'Items.txt')
    items, weights = load_items(file_path)

    if not items:
        return jsonify({"error": "No items loaded"}), 500

    item_result = random.choices(items, weights=weights, k=1)[0]

    return jsonify({"item": item_result})

@app.route("/Battle")
def battle():
    if not session.get("userId"):
        return redirect("/Login")
    res = requests.get(f"{app.config["BASE_URL"]}/Item")
    items = [
        item for item in res.json()
        if item["id"] is not None
    ]

    res = requests.get(f"{app.config["BASE_URL"]}/itemEnums")
    enums = res.json()

    item_categories = enums.get("ItemCategoryEnum", {})
    shop_tiers = enums.get("ShopTierEnum", {})

    res = requests.get(f"{app.config["BASE_URL"]}/addMove")

    context = {
        "gameId": session.get("gameId"),
        "items": items,
        "item_categories": item_categories,
        "shop_tiers": shop_tiers,
        "baseUrl": app.config["BASE_URL"],
        "moveData": res.json(),
    }
    return render_template("battle.html", **context)

def Item(request):
    item_result = None
    file_path = os.path.join(os.path.dirname(__file__), 'Items.txt')  # Adjust if your file is in a different folder

    if request.method == 'POST':
        items, weights = load_items(file_path)
        if items:
            item_result = random.choices(items, weights=weights, k=1)[0]

    context = {
        "item_result": item_result
    }
    return

@app.route("/Move", methods=["GET", "POST"])
def move():
    if request.method == "POST":
        data = request.form.to_dict()
        print("hit")
        res = requests.post(f"{app.config["BASE_URL"]}/addMove", json=data)

    res = requests.get(f"{app.config["BASE_URL"]}/addMove")
    # print(res)
    context = {
        "gameId": session.get("gameId"),
        "data": res.json()
    }
    return render_template("add_move.html", **context)

@app.route("/Item", methods=["GET"])
def item():
    res = requests.get(f"{app.config["BASE_URL"]}/itemEnums")
    enums = res.json()

    item_categories = enums.get("ItemCategoryEnum", {})
    shop_tiers = enums.get("ShopTierEnum", {})

    context = {
        "item_categories": item_categories,
        "shop_tiers": shop_tiers,
        "baseUrl": app.config["BASE_URL"]
    }

    return render_template("item.html", **context)

SHOP_TIER_MAPPING = {
    "Basic Tier": 1,
    "Common Tier": 2,
    "Advanced Tier": 3,
    "Elite Tier": 4,
    "Expert Tier": 5,
    "Legendary Tier": 6,
    "Mythic Tier": 7,
    "Divine Tier": 8,
}

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run('0.0.0.0', 8000, debug=True)

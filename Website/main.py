from flask import Flask, render_template, request, redirect, session
from .instance.config import DevelopmentConfig
import requests

app = Flask(__name__)
app.secret_key = "Fuck_You_Sessions"
app.config.from_object(DevelopmentConfig)

def contextExample():
    context = {
        "data": "banana",
    }
    return render_template('ayayay.html', **context)

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
    if session.get("playerGuid"):
        return render_template("player.html", gameId=session.get("gameId"), pokemonGuid=session.get("playerGuid"), baseUrl=app.config["BASE_URL"])

@app.route("/ItemShop")
def itemShop():
    res = requests.get(f"{app.config["BASE_URL"]}/item")
    items = [
        item for item in res.json()
        if item["id"] is not None
    ]

    context = {
         "items": items, 
         "playerGuid": session.get("playerGuid"), 
         "gameId": session.get("gameId"),
         "baseUrl": app.config["BASE_URL"]
    }

    return render_template("item_shop.html", **context)

@app.route("/Battle")
def battle():
    res = requests.get(f"{app.config["BASE_URL"]}/item")
    items = [
        item for item in res.json()
        if item["id"] is not None
    ]

    res = requests.get(f"{app.config["BASE_URL"]}/itemEnums")
    enums = res.json()

    item_categories = enums.get("ItemCategoryEnum", {})
    shop_tiers = enums.get("ShopTierEnum", {})

    context = {
        "gameId": session.get("gameId"),
        "items": items,
        "item_categories": item_categories,
        "shop_tiers": shop_tiers,
        "baseUrl": app.config["BASE_URL"]
    }
    return render_template("battle.html", **context)

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

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run('0.0.0.0', 8000, debug=True)

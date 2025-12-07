from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)
app.secret_key = "Fuck_You_Sessions"
url = "http://127.0.0.1:9000/"

def contextExample():
    context = {
        "data": "banana",
    }
    return render_template('ayayay.html', **context)

@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        data = {
            "username": username,
            "password": password
        }

        res = requests.post("http://127.0.0.1:9000/login", json=data)
        res = res.json()

        # If login was successful, store user_id in session
        if "userId" in res:
            session["userId"] = res["userId"]
        if "gameId" in res:
            session["gameId"] = res["gameId"]
        print(session.get("userId"))
        print(session.get("gameId"))

        return redirect('/Game')
        return render_template('login.html', message=res.get("message", "No Message Recieved"))

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

        res = requests.post("http://127.0.0.1:9000/register", json=data)
        res = res.json()
        return redirect('/Login')
    return render_template('register.html')

@app.route('/')
def addPokemon():
    context = {
        "gameId": session.get("gameId"),
    }
    return render_template('add_pokemon.html', **context)


@app.route('/Game')
def game():
    context = {
        "gameId": session.get("gameId")
    }
    return render_template('game.html', **context)

@app.route("/Battle")
def battle():
    context = {
        "gameId": session.get("gameId")
    }
    return render_template("battle.html", **context)

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run('0.0.0.0', 8000, debug=True)

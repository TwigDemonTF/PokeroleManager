from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "user": "Twigdemon"
    }

    return render_template('index.html', **context)

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run('0.0.0.0', 8000, debug=True)

from flask import Flask, render_template

app = Flask(__name__)


def contextExample():
    context = {
        "data": "banana",
    }
    return render_template('ayayay.html', **context)

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/Register')
def register():
    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run('0.0.0.0', 8000, debug=True)

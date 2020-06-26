import os

from flask import Flask, send_from_directory
from flask import render_template as render

app = Flask(__name__)


@app.route('/')
def index():
    return render('index.html')


@app.route('/game')
def game():
    return render('game.html')


@app.route('/cheat')
def cheat():
    return render('cheat.html')


@app.route('/purchases')
def hello_world3():
    return render('purchases.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)

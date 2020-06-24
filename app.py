from flask import Flask
from flask import render_template as render

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render('index.html')

@app.route('/game')
def hello_world1():
    return render('game.html')


if __name__ == '__main__':
    app.run(debug=True)

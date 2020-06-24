from flask import Flask
from flask import render_template as render

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render('index.html')


if __name__ == '__main__':
    app.run()

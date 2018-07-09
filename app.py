from flask import Flask

app = Flask(__name__)

PORT = 4390


@app.route('/')
def homepage():
    return "Howdy hacker!"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

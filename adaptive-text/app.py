from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/adaptiveTextDB"
mongo = PyMongo(app)


@app.route('/')
def index():
    return "Hello, World! from app2"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

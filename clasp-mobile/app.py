from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/claspMobileDB"
mongo = PyMongo(app)


@app.route('/')
def index():
    return "Hello, World! from app1"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

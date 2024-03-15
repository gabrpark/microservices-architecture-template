from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# mongo = PyMongo(app)


@app.route('/')
def index():
    return "API for CLASP is running!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

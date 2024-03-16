import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_URI"] = "mongodb://localhost:27017/adaptiveTextDB"
mongo = PyMongo(app)


# Default route
@app.route('/')
def index():
    return "API for AdaptiveText is running!"

# GET endpoint for AdaptiveText's "sourceTexts" collection


@app.route('/api')
def get_source_text():
    # AdaptiveText Database
    source_texts_collection = mongo.db.sourceTexts
    # Directly use the reference to the desired collection
    data = list(source_texts_collection.find({}, {'_id': 0}))
    return jsonify(data)

# GET endpoint for AdaptiveText's "sourceTexts" collection


# @app.route('/api/v1/adaptivetext/sourcetexts', methods=['GET'])
# def get_source_texts():
#     data = list(source_texts.find({}, {'_id': 0}))
#     return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

from pymongo import MongoClient
import os


class ResponseModel:
    def __init__(self):
        self.db = MongoClient(os.environ.get("MONGO_URI")).claspMobileDB
        self.collection = self.db['responses']

    def find_all(self, query):
        documents = list(self.collection.find(query, {'_id': 0}))
        return documents

    def insert(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

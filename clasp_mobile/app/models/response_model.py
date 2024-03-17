import os
from app.utils.db import get_db
from pymongo import MongoClient


class ResponseModel:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['responses']

    def find_all(self, query):
        documents = list(self.collection.find(query, {'_id': 0}))
        return documents

    def insert(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

import os
# from bson import ObjectId
from app.utils.db import get_db
from pymongo import MongoClient


class TaskModel:
    def __init__(self):
        # self.db = MongoClient(os.environ.get("MONGO_URI")).claspMobileDB
        # self.collection = self.db['tasks']
        self.db = get_db()
        self.collection = self.db['tasks']

    def find_all(self, query):
        documents = list(self.collection.find(query, {'_id': 0}))
        return documents

    # def insert(self, data):
    #     result = self.collection.insert_one(data)
    #     return str(result.inserted_id)

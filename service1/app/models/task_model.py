import os
# from bson import ObjectId
from app.utils.db import get_db
from pymongo import MongoClient


class TaskModel:
    '''
    This class is responsible for interacting with the tasks collection in the database.
    '''

    def __init__(self):
        # self.db = MongoClient(os.environ.get("MONGO_URI")).claspMobileDB
        # self.collection = self.db['tasks']
        self.db = get_db()
        self.collection = self.db['tasks']

    def find_all(self, query):
        '''
        This method finds all tasks in the database that match the given query.

        Args:
            query (dict): The query to use to find tasks.

        Returns:
            list: A list of tasks that match the given query.
        '''
        documents = list(self.collection.find(query, {'_id': 0}))
        return documents

    # def insert(self, data):
    #     result = self.collection.insert_one(data)
    #     return str(result.inserted_id)

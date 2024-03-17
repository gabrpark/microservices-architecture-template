import os
from app.utils.db import get_db
from pymongo import MongoClient


class ResponseModel:
    '''
    Class for interacting with the responses collection in the database.
    '''

    def __init__(self):
        self.db = get_db()
        self.collection = self.db['responses']

    def find_all(self, query):
        '''
        Finds all documents in the responses collection that match the given query.

        Args:
            query (dict): The query to use to find documents.

        Returns:
            list: A list of documents that match the query.
        '''
        documents = list(self.collection.find(query, {'_id': 0}))
        return documents

    def insert(self, data):
        '''
        Inserts a new document into the responses collection.

        Args:
            data (dict): The data to insert into the collection.

        Returns:
            str: The ID of the inserted document.
        '''
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

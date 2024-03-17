import os
from bson import ObjectId
from app.utils.db import get_db
from pymongo import MongoClient

db = get_db()
collection = db['sourceTexts']


class TextModel:
    def __init__(self, title, content, url, _id=None):
        self.title = title
        self.content = content
        self.url = url
        self._id = _id

    # def save(self):
    #     result = collection.insert_one(self.to_dict())
    #     self._id = result.inserted_id
    #     return result

    @staticmethod
    def get_all(args):
        documents = list(collection.find(args, {'_id': 0}))
        return documents

    # @staticmethod
    # def get_by_id(text_id):
    #     document = collection.find_one({'_id': ObjectId(text_id)}, {'_id': 0})
    #     return document

    # def update(self):
    #     collection.update_one({'_id': ObjectId(self._id)}, {
    #                           '$set': self.to_dict()})

    # @staticmethod
    # def delete_by_id(text_id):
    #     result = collection.delete_one({'_id': ObjectId(text_id)})
    #     return result

    # def to_dict(self):
    #     return {'title': self.title, 'content': self.content, 'url': self.url, '_id': self._id}

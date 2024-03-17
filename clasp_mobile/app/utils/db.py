from pymongo import MongoClient
import os


def get_db():
    # Get the MongoDB connection string from the environment variable
    mongo_uri = os.environ.get('LOCAL_MONGO_URI')

    if not mongo_uri:
        raise ValueError('LOCAL_MONGO_URI environment variable is not set')

    # Create a MongoClient instance
    client = MongoClient(mongo_uri)

    # Get the database name from the environment variable
    db_name = os.environ.get('MONGO_DB_NAME')

    if not db_name:
        raise ValueError('MONGO_DB_NAME environment variable is not set')

    # Get the database instance
    db = client[db_name]

    return db

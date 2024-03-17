from pymongo import MongoClient
from app.utils.db import get_db

db = get_db()

# Initialize collections for service1
collection1 = db['sourceTexts']
if collection1.count_documents({}) == 0:
    collection1.insert_many([
        {
            "title": "Hodge Conjecture",
            "content": "[TEST] In mathematics, the Hodge conjecture is a major unsolved problem in algebraic geometry and complex geometry that relates the algebraic topology of a non-singular complex algebraic variety to its subvarieties.",
            "url": "https://en.wikipedia.org/wiki/Hodge_conjecture"
        }
    ])

print("Data inserted successfully.")

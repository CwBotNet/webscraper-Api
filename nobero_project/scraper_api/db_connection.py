import os
from pymongo import MongoClient

class MongoDB:
    def __init__(self, db_name):
        CONNECTION_STRING = os.environ.get("DATABASE_URL")
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client["nobero_products"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

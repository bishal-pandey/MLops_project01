import os
import sys
import pymongo
import certifi

from src.exception import CustomException
from src.logger import logging
from src.constants import DATABASE_NAME, COLLECTION_NAME, MONGO_CONNECTION_URL

class MongoDBConnection:
    '''MongoDBConnection class establish the connection to mongodb database'''

    client = None

    def __init__(self,database_name=DATABASE_NAME):
        try:
            if MongoDBConnection.client is None:
                mongo_db_url = os.getenv(MONGO_CONNECTION_URL)
                print(MONGO_CONNECTION_URL)
                if mongo_db_url is None:
                    raise Exception("MongoDB URL not found")
                MongoDBConnection.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=certifi.where())
            self.client = MongoDBConnection.client
            self.database = self.client[database_name]
            logging.info(f"Connected to MongoDB database: {database_name}")
        except Exception as e:
            raise CustomException(e,sys)
        


MongoDBConnection()
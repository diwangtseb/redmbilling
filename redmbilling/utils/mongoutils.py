from pymongo import MongoClient
from redmbilling.config.mongo_config import MongoInfo 

client = MongoClient(host=MongoInfo.host,port=MongoInfo.port)

db = client.test_mongodb

collection = db.test_collection

print(collection)

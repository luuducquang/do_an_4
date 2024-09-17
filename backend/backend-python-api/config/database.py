from pymongo import MongoClient

uri = "mongodb://localhost:27017/QuangComesticDatabase"
client = MongoClient(uri)
database = client.get_database()

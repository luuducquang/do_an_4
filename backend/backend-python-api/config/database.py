from pymongo import MongoClient

uri = "mongodb://localhost:27017/doan4_luuducquang_bida"
client = MongoClient(uri)
database = client.get_database()

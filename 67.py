import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

for i in collection.find({'aliases.name':'OASIS'}):
    print(i)

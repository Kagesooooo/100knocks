import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

for i in collection.find({'tags.value':'dance'}).sort('rating.count',-1).limit(10):
    print(i.get('name'))

import json
import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

with open('artist.json') as f:
    for l in f:
        js = json.loads(l)
        collection.insert_one(js)

collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])

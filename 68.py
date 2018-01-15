import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

cnt = 0
for i in collection.find({'tags.value':'dance'}).sort('rating.count',-1).limit(10):
    cnt += 1
    print(str(cnt) + '\t' + i.get('name'))

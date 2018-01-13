import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

cnt = 0
for i in collection.find({'area':'Japan'}):
    cnt += 1
print(cnt)

# db.artist.find({'area':'Japan'}).count();


import plyvel
import json

db = plyvel.DB('./plyveldb/', create_if_missing=True)

js = json.dumps({'foo': {'bar': ('baz', None, 1.0, 2)}})
db.put(b'key1', js.encode())

js = json.dumps({'ham': 'egg'})
db.put(b'key2', js.encode())

for keydata, val in db:
    print(keydata)
    print(json.loads(val.decode()))

readdata = json.loads(db.get(b'key1').decode())
print(readdata)

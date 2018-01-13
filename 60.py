import plyvel
import json

db = plyvel.DB('./db_test/', create_if_missing=True)

with open('artist.json')as f:
    for l in f:
        js = json.loads(l)
        key = js['name'] +' ' + str(js['id'])
        value = js.get('area')
        if value == None:
            value = 'None'
        db.put(key.encode(), value.encode())

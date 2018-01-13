import plyvel
import json

db = plyvel.DB('./plyvel_tag/', create_if_missing=True)

# with open('artist.json')as f:
#     for l in f:
#         js = json.loads(l)
#         key = js['name'] +' ' + str(js['id'])
#         list0 = js.get('tags')
#         if list0 == None:
#             list0 = []
#         db.put(key.encode(), json.dumps(list0).encode())

for key, value in db:
    if key == 'WIK▲N 805192'.encode():
        print(value)

import plyvel
import json

db = plyvel.DB('./plyvel_tag/', create_if_missing=True)

# with open('artist.json')as f:
#     for l in f:
#         js = json.loads(l)
#         key = js['name'] + '\t' + str(js['id'])
#         list0 = js.get('tags')
#         if list0 == None:
#             list0 = []
#         db.put(key.encode(), json.dumps(list0).encode())

cnt = 0
for key, value in db:
    if 'Oasis' == (key.decode()).split('\t')[0]:
        cnt += 1
        print('No.' + str(cnt))
        str0 = ''
        for v in json.loads(value.decode()):
            str0 += '\t' + v.get('value') + '\t' + str(v.get('count')) + '\n'
        if str0 == '':
            print('None')
        else:
            print(str0[:-1])

import json

f = open('jawiki-country.json')

jdata = []
eng = 0
for i, s in enumerate(f.readlines()):
    jdata.append(json.loads(s))
    if jdata[i]['title'] == 'イギリス':
        eng = i
        break

print(jdata[eng]['text'])

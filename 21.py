import json

f = open('jawiki-country.json')

jdata = []
eng = 0
for i, s in enumerate(f.readlines()):
    jdata.append(json.loads(s))
    if jdata[i]['title'] == 'イギリス':
        eng = i

text = jdata[eng]['text'].split('\n')

for s in text:
    if 'Category' in s:
        print(s)

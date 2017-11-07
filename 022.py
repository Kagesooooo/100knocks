import json

with open('jawiki-country.json', 'r') as f:
    rd = f.readlines()

jdata = []
eng = 0

for i in range(len(rd)):
    jdata.append(json.loads(rd[i]))
    if jdata[i]['title'] == 'イギリス':
        eng = i
text = jdata[eng]['text'].split('\n')

for s in text:
    if 'Category' in s:
        print((s.lstrip('[Category:')).rstrip('|*]'))

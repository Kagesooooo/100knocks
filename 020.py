import json

with open('jawiki-country.json', 'r') as f:
    rd = f.readlines()

jdata = []
eng = 0

for i in range(len(rd)):
    jdata.append(json.loads(rd[i]))
    if jdata[i]['title'] == 'イギリス':
        eng = i

print(jdata[eng]['text'])

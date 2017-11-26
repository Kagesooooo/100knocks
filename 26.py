import json
import re

f = open('jawiki-country.json')

jdata = []
eng = 0
for i, s in enumerate(f.readlines()):
    jdata.append(json.loads(s))
    if jdata[i]['title'] == 'イギリス':
        eng = i
        break

text = jdata[eng]['text'].split('\n')

flag = 0
dic = {}
field = ''
for i, s in enumerate(text):
    s = re.sub(r"('''|'')",'',s)
    if s[0:2] == '{{' and '基礎情報' in s:
        flag = 1
        continue
    if s == '}}':
        break
    if flag == 1:
        match = re.search(r'^\|(.*?) = (.*?)$',s)
        if match != None:
            field = match.group(1)
            dic[field] = match.group(2)
        else:
            dic[field] += '\n' + s

for k,v in dic.items():
    print(k,v)

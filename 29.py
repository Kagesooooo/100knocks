import json
import re
import urllib, urllib.request

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
    s = re.sub(r"('''|'')","",s)
    if s[0:2] == '{{' and '基礎情報' in s:
        flag = 1
        continue
    if s == '}}':
        break
    if flag == 1:

        link_rm = re.search(r'\[{2}(.*?)(\|(.*?)|)(\|(.*?)|)\]{2}',s)
        if link_rm != None:
            if link_rm.group(5) != None:
                s = re.sub(r'\[{2}(.*?)\|(.*?)\|(.*?)\]{2}',link_rm.group(5),s)
            elif link_rm.group(3) != None:
                s = re.sub(r'\[{2}(.*?)\|(.*?)\]{2}',link_rm.group(3),s)
            else:
                s = re.sub(r'(\[{2}|\]{2})','',s)

        lang_rm = re.search(r'\{{2}(.*?)(\|(.*?)|)(\|(.*?)|)\}{2}',s)
        if lang_rm != None:
            if lang_rm.group(5) != None:
                s = re.sub(r'\{{2}(.*?)\|(.*?)\|(.*?)\}{2}',lang_rm.group(5),s)
            elif lang_rm.group(3) != None:
                s = re.sub(r'\{{2}(.*?)\|(.*?)\}{2}',lang_rm.group(3),s)
            else:
                s = re.sub(r'(\{{2}|\}{2})','',s)

        s = re.sub(r'^\*+','',s)
        s = re.sub(r'\[+(.*?)\]+','',s)
        s = re.sub(r'\<+(.*?)\>+','',s)


        match = re.search(r'^\|(.*?) = (.*?)$',s)
        if match != None:
            field = match.group(1)
            dic[field] = match.group(2)
        else:
            dic[field] += '\n' + s



s = urllib.parse.quote(dic['国旗画像'])

url = 'http://ja.wikipedia.org/w/api.php?'

url += 'format=json&action=query&prop=imageinfo&iiprop=url&titles=File:' + s

req = urllib.request.Request(url)

f = urllib.request.urlopen(req)

d = json.loads(f.read().decode('utf-8'))

print(d['query']['pages']['-1']['imageinfo'][0]['url'])

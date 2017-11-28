import re

with open('neko.txt.mecab')as f:
    dic = {}
    for s in f:
        if re.search('EOS',s):
            break
        line = re.split(r'[\t,]',s[:-1])
        dic['surface'] = line[0]
        dic['pos'] = line[1]
        if dic['pos'] == '動詞':
            print(dic['surface'])

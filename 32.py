import re

with open('neko.txt.mecab')as f:
    dic = {}
    for s in f:
        if re.search('EOS',s):
            break
        line = re.split(r'[\t,]',s[:-1])
        dic['base'] = line[7]
        dic['pos'] = line[1]
        if dic['pos'] == '動詞':
            print(dic['base'])

import re

with open('neko.txt.mecab')as f:
    dic = {}
    pre = {}
    flag = 0
    for s in f:
        if re.search('EOS',s):
            break
        line = re.split(r'[\t,]',s[:-1])
        dic['surface'] = line[0]
        dic['pos'] = line[1]
        if flag == 1 and dic['pos'] == '名詞':
            print(st + 'の' + dic['surface'])
        if dic['surface'] == 'の' and pre['pos'] == '名詞':
            st = pre['surface']
            flag = 1
        else:
            flag = 0
        pre = dic.copy()

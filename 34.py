import re

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    dic = {}
    pre = {}
    flag = False
    for s in f:
        match = pattern.match(s)
        if match == None:
            continue
        dic['surface'] = match.group(1)
        dic['pos'] = match.group(2)
        if flag == True and dic['pos'] == '名詞':
            print(st + 'の' + dic['surface'])
        if dic['surface'] == 'の' and pre['pos'] == '名詞':
            st = pre['surface']
            flag = True
        else:
            flag = False
        pre = dic.copy()

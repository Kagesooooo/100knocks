import re

with open('neko.txt.mecab')as f:
    dic = {}
    i = 0
    list0 = [[]]
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    for s in f:
        match = pattern.match(s)
        if match == None:
            break
        dic['surface'] = match.group(1)
        dic['base'] = match.group(8).split(',')[0]
        dic['pos'] = match.group(2)
        dic['pos1'] = match.group(3)
        list0[i].append(dic.copy())
        if dic['surface'] == '。':
            i += 1
            list0.append([])
print(list0)

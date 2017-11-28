import re

with open('neko.txt.mecab')as f:
    dic = {}
    i = 0
    flag = 0
    list0 = [[]]
    for s in f:
        if re.search('EOS',s):
            break
        if flag == 1:
            i += 1
            list0.append([])
        line = re.split(r'[\t,]',s[:-1])
        dic['surface'] = line[0]
        dic['base'] = line[7]
        dic['pos'] = line[1]
        dic['pos1'] = line[2]
        if dic['pos'] == '記号':
            flag = 1
        else:
            flag = 0
        list0[i].append(dic.copy())
print(list0)

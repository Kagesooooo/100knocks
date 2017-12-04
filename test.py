import re

with open('neko.txt.mecab')as f:
    dic = {}
    # i = 0
    list0 = [[]]
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    for s in f:
        match = pattern.match(s)
        if match == None:
            if len(list0[-1]) != 0:
                # i += 1
                list0.append([])
                print()
        continue
        dic['surface'] = match.group(1)
        dic['base'] = match.group(8).split(',')[0]
        dic['pos'] = match.group(2)
        dic['pos1'] = match.group(3)
        print(dic['surface'],dic['base'],dic['pos'],dic['pos1'])
        list0[-1].append(dic.copy())
        # if dic['surface'] == '。':
        #     i += 1
        #     list0.append([])
        #     print()
        for v in dic.values():
            st += v
        print(st)

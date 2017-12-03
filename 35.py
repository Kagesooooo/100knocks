import re

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    dic = {}
    st = ''
    cnt = 0
    for s in f:
        match = pattern.match(s)
        if match == None:
            break
        dic['surface'] = match.group(1)
        dic['pos'] = match.group(2)
        if dic['pos'] == '名詞':
            st += dic['surface']
            cnt += 1
        else:
            if st != '' and cnt > 1:
                print(st)
            cnt = 0
            st = ''

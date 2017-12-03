import re

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    dic = {}
    st = ''
    for s in f:
        match = pattern.match(s)
        if match == None:
            break
        dic['surface'] = match.group(1)
        dic['pos'] = match.group(2)
        if dic['pos'] == '名詞':
            st += dic['surface']
        else:
            if st != '':
                print(st)
            st = ''

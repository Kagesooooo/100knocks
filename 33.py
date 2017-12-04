import re

with open('../Downloads/neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    for s in f:
        match = pattern.match(s)
        if match == None:
            continue
        if match.group(2) == '名詞':
            if match.group(3) == 'サ変接続':
                print(match.group(1))

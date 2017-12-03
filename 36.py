import re

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    wd_dic = {}
    for s in f:
        match = pattern.match(s)
        if match == None:
            break
        sur = match.group(1)
        if sur not in wd_dic:
            wd_dic[sur] = 1
        else:
            wd_dic[sur] += 1

for k, v in sorted(wd_dic.items(), key=lambda x: -x[1]):
    print(k + " " + str(v))

import re

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    wd_dic = {}
    for s in f:
        match = pattern.match(s)
        # if match == None:
        #     break
        if match == None:
            continue
        sur = match.group(1)
        if sur not in wd_dic:
            wd_dic[sur] = 1
        else:
            wd_dic[sur] += 1

cnt = 0
for k, v in sorted(wd_dic.items(), key=lambda x: (-x[1],x[0])):
    if cnt == 99 or cnt == 199:
        print(k + " " + str(v))
    cnt += 1

print(cnt)

# print(wd_dic)

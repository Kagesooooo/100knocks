import numpy as np
from collections import defaultdict

with open('output/94.txt')as f:
    sens = f.readlines()

unko = []
human = []
n = 0
unko_dic = defaultdict(float)
human_dic = defaultdict(float)
tups = []
for sen in sens:
    words = sen.split('\t')
    tup = (words[0],words[1])
    human_dic[tup] = float(words[2])
    unko_dic[tup] = float(words[3])
    tups.append(tup)
    n += 1

cnt = 0
unko_index = defaultdict(int)
for key,value in sorted(unko_dic.items(), key=lambda x: x[1]):
    unko_index[key] = cnt
    cnt += 1

cnt = 0
human_index = defaultdict(int)
for key,value in sorted(human_dic.items(), key=lambda x: x[1]):
    human_index[key] = cnt
    cnt += 1

sum = 0
for key in tups:
    sum += pow(human_index[key]-unko_index[key], 2)
result = 1-(6*sum)/(pow(cnt,3)-cnt)

print(result)

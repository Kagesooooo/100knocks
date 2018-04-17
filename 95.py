import numpy as np

with open('output/94.txt')as f:
    sens = f.readlines()

model = []
human = []
cnt = 0
for sen in sens:
    words = sen.split('\t')
    human.append(float(words[2]))
    model.append(float(words[3]))
    cnt += 1

total = 0
for i in range(cnt):
    total += pow(human[i]-model[i], 2)
result = 1 - (6 * total) / (pow(cnt, 3) - cnt)

print(result)

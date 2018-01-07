from stemming.porter2 import stem
import re

with open('output/51.txt')as fi:
    with open('output/52.txt','w')as fo:
        for l in fi:
            fo.write(l[:-1] + '\t' + stem(l[:-1]) + '\n')

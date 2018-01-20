import func8
from collections import defaultdict

with open('sentiment.txt',encoding='latin-1')as f:
    word_dic = func8.mk_word_dic(f)

for key, value in word_dic.items():
    if value > 20 and value < 100:
        print(key)

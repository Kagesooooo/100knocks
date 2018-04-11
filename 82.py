import random

word_lists = []
with open('enwiki2.txt')as f:
    for sen in f:
        word_list = []
        for word in sen.split():
            word_list.append(word)
        word_lists.append(word_list)

for word_list in word_lists:
    list_len = len(word_list)
    for i,word in enumerate(word_list):
        num = random.randint(1,5)
        for j in range(num):
            if i-j > 0:
                print(word+'\t'+word_list[i-j-1])
            if i+j+1 < list_len:
                print(word+'\t'+word_list[i+j+1])

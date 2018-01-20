from stop_words import get_stop_words
from collections import defaultdict
from stemming.porter2 import stem
import math

def stop_func(str0):
    return str0 in get_stop_words('english')

def mk_word_dic(f):
    word_dic = defaultdict(int)
    for sen in f:
        for w in sen[3:-1].split():
            w = stem(w)
            if stop_func(w):
                continue
            else:
                word_dic[w] += 1
    return word_dic

def mk_lines(f):
    list0 = []
    for l in f:
        list1 = l.strip('\n').split()
        list2 = []
        if list1[0] == '+1':
            list2.append('1')
        else:
            list2.append('0')
        for word in list1[1:]:
            if stop_func(word):
                continue
            else:
                list2.append(stem(word))
        list0.append(list2)
    return list0

def update(W, X, l, eta):
    a = sum([W[x] for x in X])
    g = ((1. / (1. + math.exp(-a))) - l) if -100. < a else (0. - l)
    for x in X:
        W[x] -= eta * g

def train(lines,eta0,loop):
    t = 1
    W = defaultdict(float)
    for i in range(loop):
        for line in lines:
            update(W, line[1:], float(line[0]), eta0 / (1 + t / float(len(lines))))
            t += 1
    return W

def predict(dic, word_list):
    cnt = 0.
    for word in word_list:
        word = stem(word)
        if word in dic:
            cnt += dic[word]
    rate = (1. / (1. + math.exp(-cnt)))
    return rate

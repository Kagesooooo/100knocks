import func8

dic = {}
with open('output/73.txt')as f:
    for l in f:
        a = l.split()
        dic[a[0]] = float(a[1])

sen = input('hai ')

rate = func8.predict(dic, sen.split())

if rate > 0.5:
    print('+1: {}'.format(rate))
else:
    print('-1: {}'.format(1-rate))

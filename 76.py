import func8

dic = {}
with open('output/73.txt')as f:
    for l in f:
        a = l.split()
        dic[a[0]] = float(a[1])

with open('sentiment.txt')as f:
    for l in f:
        sen = l.strip('\n').split()
        rate = func8.predict(dic, sen[1:])
        if rate > 0.5:
            print('{}\t+1\t{}'.format(sen[0],rate))
        else:
            print('{}\t-1\t{}'.format(sen[0],1-rate))

import func8

with open('sentiment.txt')as f:
    read = f.readlines()
list0 = func8.mk_lines(read)

# fo = open('data_file.txt','w')

eta0 = 0.1
loop = 10
length = len(list0)
cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0

lines = []
a = []
for k in range(5):
    lines.append([line for i, line in enumerate(list0) if i < k*length/5 or i > (k+1)*length/5])
    a.append(func8.train(lines[k],eta0,loop))
    for i, l in enumerate(read):
        if i < k*length/5 or i > (k+1)*length/5:
            continue
        sen = l.strip('\n').split()
        rate = func8.predict(a[k], sen[1:])
        if rate > 0.5:
            # fo.write(str(sen[0])+'\t+1\t'+str(rate)+'\n')
            # print('{}\t+1\t{}'.format(sen[0],rate))
            if sen[0] == '+1':
                cnt0 += 1
            else:
                cnt2 += 1
        else:
            # fo.write(str(sen[0])+'\t-1\t'+str(rate)+'\n')
            # print('{}\t-1\t{}'.format(sen[0],1-rate))
            if sen[0] == '+1':
                cnt1 += 1
            else:
                cnt3 += 1

correct = (cnt0+cnt3)/(cnt0+cnt1+cnt2+cnt3)
com = cnt0/(cnt0+cnt2)
rep = cnt0/(cnt0+cnt1)
f1 = 2*(com*rep)/(com+rep)

print('正解率: {}'.format(correct))
print('適合率: {}'.format(com))
print('再現率: {}'.format(rep))
print('F1: {}'.format(f1))

# fo.close()

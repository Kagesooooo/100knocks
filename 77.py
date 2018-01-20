f = open('output/76.txt')

cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
for l in f:
    list0 = l.strip('\n').split('\t')
    if list0[0] == '+1':
        if list0[1] == '+1':
            cnt0 += 1
        else:
            cnt1 += 1
    else:
        if list0[1] == '+1':
            cnt2 += 1
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

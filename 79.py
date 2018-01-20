import numpy as np
import matplotlib.pyplot as plt

with open('data_file.txt')as f:
    data_list = f.readlines()

# print(len(data_list))

i_list = []
coms = []
reps = []

list1 = []
for l in data_list:
    list0 = l.strip('\n').split('\t')
    list0[2] = float(list0[2])
    list1.append(list0)

for i in np.arange(0.02,1.0,0.05):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for l in list1:
        rate = float(l[2])
        if rate > i:
            if l[0] == '+1':
                cnt0 += 1
            else:
                cnt2 += 1
        else:
            if l[0] == '+1':
                cnt1 += 1
            else:
                cnt3 += 1
    # print(cnt0,cnt1,cnt2,cnt3)

    i_list.append(i)
    coms.append(cnt0/(cnt0+cnt2))
    reps.append(cnt0/(cnt0+cnt1))

plt.plot(i_list,coms)
plt.plot(i_list,reps)
plt.show()





# correct = (cnt0+cnt3)/(cnt0+cnt1+cnt2+cnt3)
# com = cnt0/(cnt0+cnt2)
# rep = cnt0/(cnt0+cnt1)
# f1 = 2*(com*rep)/(com+rep)

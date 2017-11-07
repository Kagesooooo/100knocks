with open('hightemp.txt','r') as f:
    list0 = sorted([s.split('\t') for s in f.readlines()], key=lambda x:x[2], reverse=False)

# print(''.join([s if (i+1)==len(list1) else s+'\t' for list1 in list0 for i,s in enumerate(list1)]))
wd=''
for list1 in list0:
    for i,s in enumerate(list1,start=1):
        if (i)==len(list1):
            wd += s
        else:
            wd += s+'\t'

print(wd)

# sort -r -n -k 3 hightemp.txt

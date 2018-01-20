dic = {}
with open('output/73.txt')as f:
    for l in f:
        a = l.split()
        dic[a[0]] = float(a[1])

print('top10')
for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True)[:10]:
    print(key,value)

print('worst10')
for key,value in sorted(dic.items(),key=lambda x:x[1])[:10]:
    print(key,value)

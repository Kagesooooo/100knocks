with open('col1.txt','r') as f:
    r0 = f.readlines()

with open('col2.txt','r') as f:
    r1 = f.readlines()

with open('region.txt','w') as f:
    [f.write(s[:-1]+'\t'+t[:-1]+'\n') for s,t in zip(r0,r1)]

#paste

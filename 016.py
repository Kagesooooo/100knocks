import sys

with open('hightemp.txt','r') as f:
    rd = f.readlines()

for i in range(len(rd)):
    print(rd[i][:-1])
    if (i+1)%(len(rd)/int(sys.argv[1]))==0:
        print()

# [print(rd[i][:-1]) if (i+1)%(len(rd)/int(sys.argv[1]))!=0 else print(rd[i][:-1]+'\n') for i in range(len(rd))]

#split -l 4 hightemp.txt

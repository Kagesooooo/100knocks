import sys

with open('hightemp.txt','r') as f:
    rd = f.readlines()

[print(rd[i][:-1]) for i in range(int(sys.argv[1]))]

# head -n 4 hightemp.txt

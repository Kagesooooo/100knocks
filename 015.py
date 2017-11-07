import sys

with open('hightemp.txt','r') as f:
    rd = f.readlines()

[print(rd[-(i+1)][:-1]) for i in reversed(range(int(sys.argv[1])))]

# tail -n 3 hightemp.txt

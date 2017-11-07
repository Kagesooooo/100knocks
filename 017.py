with open('hightemp.txt','r') as f:
    rd = f.readlines()

set0 = {rd[i].split('\t')[0] for i in range(len(rd))}

print(set0)

# cat hightemp.txt | cut -f1 | sort | uniq

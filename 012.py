rd = open('hightemp.txt','r')
w0 = open('col1.txt','w')
w1 = open('col2.txt','w')

read = rd.readlines()

list = [read[i].split('\t') for i in range(len(read))]

[(w0.write(list[i][0]+'\n'), w1.write(list[i][1]+'\n')) for i in range(len(list))]

# cut -f 1 hightemp.txt

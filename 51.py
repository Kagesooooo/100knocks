with open('output/50.txt')as f:
    with open('output/51.txt','w')as fo:
        for l in f:
            for st in l.split():
                fo.write(st+'\n')
            fo.write('\n')

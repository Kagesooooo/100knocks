with open('nations.txt')as f:
    nations = [nation[:-1] for nation in f.readlines()]
with open('enwiki.txt')as f1:
    with open('enwiki2.txt','w')as f2:
        for sen in f1:
            unko = sen[:-1]
            for nation in nations:
                unko = unko.replace(nation,nation.replace(' ','_'))
            f2.write(unko+'\n')

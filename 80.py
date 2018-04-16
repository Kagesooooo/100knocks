f = open('enwiki-20150112-400-r100-10576.txt')
fo = open('enwiki.txt','w')
rm = '.,!?;:()[]\'\"'

word_list = []
for sen in f:
    str0 = ''
    for word in sen.split():
        # if word[0] in rm:
        #     word = word[1:]
        # if len(word) == 0:
        #     continue
        # if word[-1] in rm:
        #     word = word[:-2]
        # if len(word) == 0:
        #     continue
        word = word.strip().strip(rm)
        if len(word) != 0:
            str0 += word + ' '
    fo.write(str0+'\n')

import re

with open('nlp.txt') as f:
    with open('output/50.txt','w') as fout:
        for l in f:
            fout.write(re.sub(r'(.+?[\.;:\?!]) ([A-Z])',r'\1 \n\2',l))
        # for l in f:
        #     pat = re.compile(r'(.+?[\.;:\?!] [A-Z])')
        #     for st in pat.split(l):
        #         if st[:-1] != '':
        #             print(st[:-1])
        #             # fout.write(st[:-1]+'\n')

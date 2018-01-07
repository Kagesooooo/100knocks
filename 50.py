import re

with open('nlp.txt') as f:
    with open('output/50.txt','w') as fout:
        for l in f:
            fout.write(re.sub(r'(.+?[\.;:\?!]) ([A-Z])',r'\1 \n\2',l))

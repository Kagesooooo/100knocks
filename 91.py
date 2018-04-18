import re

with open('analogy.txt')as f:
    sen = f.read()

family = re.findall(r': family(.*?): ',sen,flags=re.DOTALL)

print(family[0][:-2])

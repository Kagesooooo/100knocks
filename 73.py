import func8

with open('sentiment.txt',encoding='latin-1')as f:
    lines = func8.mk_lines(f)

eta0 = 0.1
loop = 10

a = func8.train(lines,eta0,loop)

for key, value in a.items():
    if value > 0.1 or value < -0.1:
        print(key,value)

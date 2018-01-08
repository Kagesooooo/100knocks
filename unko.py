with open('unko.txt')as f1:
    content = f1.read()
    with open('output/56.txt')as f2:
        content1 = f2.read()
        for s,t in zip(content,content1):
            print(s,t)
            if s != t:
                break

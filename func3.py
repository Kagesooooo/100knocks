def file_in():
    with open('neko.txt.mecab')as f:
        return f.read()

print(file_in)

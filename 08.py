str0 = 'aiuEO-^/!!$keko'

def cipher(st):
    str1 = ''
    for s in st:
        if s.islower():
            str1 += chr(219-ord(s))
        else:
            str1 += s
    return str1

print(str0)
print(cipher(str0))
print(cipher(cipher(str0)))

str0 = 'I am an NLPer'

def word_bigram(str1,n):
    str_list = str1.split()
    wd_bi = []
    for i in range(len(str_list)-(n-1)):
        wd_bi.append(str_list[i:i+n])
    return wd_bi

def char_bigram(str1,n):
    char_bi = []
    for i in range(len(str1)-(n-1)):
        char_bi.append(str1[i:i+n])
    return char_bi

print(word_bigram(str0,2))
print(char_bigram(str0,2))

import random

str0 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def func(st0):
    st1 = ''
    str_list = st0.split()
    for st in str_list:
        if len(st)>4:
            st1 += ran(st)
        else:
            st1 += st
        st1 += ' '
    return st1

def ran(st):
    list0 = []
    s_begin = st[0]
    s_end = st[-1]
    for s in st[1:-1]:
        list0.append(s)
    random.shuffle(list0)
    st = s_begin
    for s in list0:
        st += s
    return st+s_end

print(func(str0))

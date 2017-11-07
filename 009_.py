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
    s = st[0] + random.shuffle(st[1:-1]) + st[-1]
    for s in list0:
        st += s
    return st+s_end

print(func(str0))

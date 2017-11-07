str0 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

str_list = str0.split()

array0 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}

i = 0

for wd in str_list:
    i += 1
    if i in array0:
        ini = wd[0]
    else:
        ini = wd[0:2]
    dic[ini] = i

print(dic)

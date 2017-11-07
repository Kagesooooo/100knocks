str0 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

str_list = str0.split()

list0 = []

remove_word = ',.'

for i in str_list:
    i = i.strip(remove_word)
    list0.append(len(i))

print(list0)

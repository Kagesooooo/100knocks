str0 = 'paraparaparadise'
str1 = 'paragraph'

st0 = str0.lstrip(str0[0])
st1 = str1.lstrip(str1[0])

x = set()
y = set()

for s,t in zip(str0,st0):
    x.add(s+t)

for s,t in zip(str1,st1):
    y.add(s+t)

print(x)
print(y)

print('和集合')
print(x|y)

print('積集合')
print(x&y)

print('差集合')
print(x-y)
print(y-x)

if 'se' in x:
    print('seはXに含まれる')
if 'se' in y:
    print('seはYに含まれる')

import math


def int2code(dec):
    r = ''
    while dec != 1:
        r += ('0' if ((dec / 2) % math.floor(dec / 2)) < 0.5 else '1')
        dec = math.floor(dec / 2)
    return r[::-1]


def getindex(collection, key):
    index = 0
    for elem in collection:
        if elem[0] == key:
            return index
        index += 1
    return -1


text = input("Key in a text!\n").lower()
l = []
for c in text:
    x = getindex(l, c)
    if x != -1:
        new_tuple = (c, l[x][1] + 1)
        l.remove((c, l[x][1]))
        l.append(new_tuple)
    else:
        l.append((c, 1))

l = sorted(l, key=lambda t: t[1], reverse=True)
code = {}
i = 2
for e in l:
    code[e[0]] = int2code(i)
    i += 1
for c in text:
    print(code[c], end=" ")
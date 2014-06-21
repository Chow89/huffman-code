import math
from binarytree import BinaryTree


def int2bin(dec):
    r = ''
    while dec > 1:
        r = str(dec % 2) + r
        dec = math.floor(dec / 2)
    return str(dec) + r


def getindex(collection, key):
    index = 0
    for elem in collection:
        if elem[0] == key:
            return index
        index += 1
    return -1


text = input("Key in a text!\n").lower()
l = []
ignore = [' ', '.', ',', ';', '!', '?', '"', "'"]
for c in text:
    if c not in ignore:
        x = getindex(l, c)
        if x != -1:
            new_tuple = (c, l[x][1] + 1)
            l.remove((c, l[x][1]))
            l.append(new_tuple)
        else:
            l.append((c, 1))

sorted_l = sorted(l, key=lambda t: t[1], reverse=True)
print(sorted_l)
b = BinaryTree('root', None, None)
i = 0
for e in sorted_l:
    print(e[0]+": "+int2bin(i))
    b.insert(e[0], int2bin(i))
    i += 1
print(b)
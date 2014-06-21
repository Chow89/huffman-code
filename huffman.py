import math


def int2bin(dec):
    r = ''
    while dec > 1:
        r = str(dec % 2) + r
        dec = math.floor(dec / 2)
    return str(dec) + r


def isin(collection, key):
    i = 0
    for e in collection:
        if e[0] == key:
            return i
        i += 1
    return -1


text = input("Key in a text!\n").lower()
l = []
ignore = [' ', '.', ',', ';', '!', '?', '"', "'"]
for c in text:
    if c not in ignore:
        x = isin(l, c)
        if x != -1:
            t = (c, l[x][1] + 1)
            l.remove((c, l[x][1]))
            l.append(t)
        else:
            l.append((c, 1))

sorted_l = sorted(l, key=lambda e: e[1], reverse=True)
print(sorted_l)
i = 0
for e in sorted_l:
    print(e[0]+": "+int2bin(i))
    i += 1
__author__ = 'Christian'


def isin(collection, key):
    i = 0
    for e in collection:
        if e[0] == key:
            return i
        i += 1
    return -1


text = input("Key in a text!\n").lower()
l = []
for c in text:
    if c != " ":
        x = isin(l, c)
        if x != -1:
            t = (c, l[x][1]+1)
            l.remove((c, l[x][1]))
            l.append(t)
        else:
            l.append((c, 1))
print(l)
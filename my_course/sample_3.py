# -*- coding: utf8 -*-

d = {}

for _ in range(int(input())):
    data = input().split()
    a, b, c = data[0], data[1], int(data[2])
    if a not in d:
        d[a] = {b: c}
    else:
        if b not in d[a]:
            d[a].update({b: c})
        else:
            d[a][b] = d[a].get(b) + c

for i in sorted(d):
    print(i + ':')
    for j in sorted(d[i]):
        print(j, d[i].get(j))


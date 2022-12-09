# -*- coding: utf8 -*-
import copy

d = {}

request = input()

for _ in range(int(input())):
    data = (input().split(': '))
    d[data[0]] = int(data[1])

answer = copy.deepcopy(request)

for i in answer:
    for j in d:
        if answer.count(i) == d.get(j):
            print(j, end='')


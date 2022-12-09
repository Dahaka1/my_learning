# -*- coding: utf8 -*-

with open('lines.txt') as file:
    lst = [i.rstrip() for i in file.readlines()]
    answer = [print(i) for i in lst if len(i) == max(map(lambda x: len(x), lst))]



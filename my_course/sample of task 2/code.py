# -*- coding: utf8 -*-

file = open('prices.txt', encoding='utf-8')

lst = [str(i).rstrip().split('\t') for i in file.readlines()]

print(sum(map(lambda x: int(x[1]) * int(x[2]), lst)))
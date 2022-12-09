# -*- coding: utf8 -*-

with open('population.txt') as file:
    lst = [i.strip().split('\t') for i in file.readlines()]
    lst = filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500000, lst)
    print(*[i[0] for i in lst], sep='\n')
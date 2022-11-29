# -*- coding: utf8 -*-

from random import *

matrix = [[0 for _ in range(5)] for _ in range(5)]
lst = list(range(1, 76))

for i in range(5):
    for j in range(5):
        matrix[i][j] = choice(lst)
        lst.remove(matrix[i][j])

matrix[2][2] = 0

for i in matrix:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()

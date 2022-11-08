# -*- coding: utf8 -*-
matrix = [['.' for _ in range(8)] for _ in range(8)]

letters = list('abcdefgh')

location = list(input())
col, row = letters.index(location[0]), 8 - int(location[1])

matrix[row][col] = 'N'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (col - j) * (row - i) == 2 or (col - j) * (row - i) == -2:
            matrix[i][j] = '*'

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
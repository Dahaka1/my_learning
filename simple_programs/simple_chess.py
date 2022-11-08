# -*- coding: utf8 -*-
from string import ascii_lowercase

matrix = [['.' for _ in range(8)] for _ in range(8)]

letters = list(ascii_lowercase[:ascii_lowercase.index('i')])

location = list(input())
col, row = letters.index(location[0]), 8 - int(location[1])

matrix[row][col] = 'N'

matrix[row - 1][col - 2] = '*' if row - 1 in range(8) and col - 2 in range(8) else '.'
matrix[row - 1][col + 2] = '*' if row - 1 in range(8) and col + 2 in range(9) else '.'
matrix[row - 2][col + 1] = '*' if row - 2 in range(8) and col + 1 in range(9) else '.'
matrix[row - 2][col - 1] = '*' if row - 2 in range(8) and col - 1 in range(8) else '.'
matrix[row + 1][col - 2] = '*' if row + 1 in range(9) and col - 2 in range(8) else '.'
matrix[row + 1][col + 2] = '*' if row + 1 in range(9) and col + 2 in range(9) else '.'
matrix[row + 2][col + 1] = '*' if row + 2 in range(9) and col + 1 in range(9) else '.'
matrix[row + 2][col - 1] = '*' if row + 2 in range(9) and col - 1 in range(8) else '.'

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
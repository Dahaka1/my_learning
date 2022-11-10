# -*- coding: utf8 -*-

matrix = [[int(_) for _ in input().split()] for _ in range(int(input()))]  # задаем квадратную матрицу с числами
ctrl = sum(matrix[0])  # контрольная сумма для проверки сумм из условия
answer = ''  # переменная с итоговым ответом, если он - 'NO'
for i in matrix:  # проверяем каждую строку матрицы
    if sum(i) != ctrl:
        answer = 'NO'
        break

count_cols = 0  # счетчик для каждого столбцов

for i in range(len(matrix)):  # проверяем каждый столбец на соответствие контрольному числу
    for j in range(len(matrix[i])):
        count_cols += matrix[j][i]
        if j == len(matrix) - 1 and count_cols == ctrl:
            count_cols = 0
        elif j == len(matrix) - 1 and count_cols != ctrl:
            answer = 'NO'

count_main_diagonal = 0  # счетчик для чисел на главной диагонали матрицы

for i in range(len(matrix)):  # аналогично проверяем главную диагональ
    count_main_diagonal += matrix[i][i]
    if matrix[i][i] == matrix[-1][-1]:
        if count_main_diagonal != ctrl:
            answer = 'NO'

count_secondary_diagonal = 0  # счетчик для чисел на побочной диагонали матрицы

for i in range(len(matrix)):  # проверяем ее
    count_secondary_diagonal += matrix[i][len(matrix) - i - 1]
if count_secondary_diagonal != ctrl:
    answer = 'NO'

if answer == 'NO':  # если ответ не приравнялся ранее к "NO", выводим "YES"
    print(answer)
else:
    print('YES')

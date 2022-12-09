# -*- coding: utf8 -*-

n = int(input())
lst = [dict() for _ in range(n)]

for i in range(n):
    for _ in range(int(input())):
        student, score = [i for i in input().split()]
        lst[i][student] = score

result = [False for _ in range(n)]

for i in range(n):
    result[i] = True if any(map(lambda x: x == '5', lst[i].values())) else False

answer = [print('YES') if all(result) else print('NO')]
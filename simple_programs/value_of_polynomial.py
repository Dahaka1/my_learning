# -*- coding: utf8 -*-

def evaluate(*coefficients, x=0):
    return list(map(lambda y: coefficients[::-1][y] * (x ** y), range(len(coefficients))))


c = [int(i) for i in input().split()]
n = int(input())

print(sum(evaluate(*c, x=n)))

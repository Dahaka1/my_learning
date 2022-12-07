# -*- coding: utf8 -*-

abscissas, ordinates, applicates = [[float(i) for i in input().split()] for _ in range(3)] # принимаем на вход неограниченное количество точек координат (x, y, z)
R = float(input()) # принимаем на вход радиус сферы

points = zip(abscissas, ordinates, applicates) # упаковываем координаты в список по соответствию осей координат
print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2  <= 4, points))) # если все точки возвращают True (сумма квадратов точек x, y, z меньше либо равна квадрату радиуса), получаем значение True, иначе - False


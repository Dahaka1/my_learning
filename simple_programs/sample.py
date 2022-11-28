# -*- coding: utf8 -*

d = {}

for _ in range(int(input())):
    data = (input().lower().split())
    d[data[0]] = data[1]  # телефон, имя

for _ in range(int(input())):
    request = input().lower()
    nums = []
    for i in d:
        if request == d.get(i):
            nums.append(i)
    if not nums:
        print('абонент не найден')
    if nums:
        print(*nums)
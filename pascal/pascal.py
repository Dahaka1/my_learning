n, m = int(input()), int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

data = [k for k in input().split()]
i, j = int(data[0]), int(data[1])

for stroke in matrix:
    stroke[i], stroke[j] = stroke[j], stroke[i]

for stroke in matrix:
    for elem in stroke:
        print(elem, end=' ')
    print()


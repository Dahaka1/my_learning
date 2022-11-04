n, m = int(input()), int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

data = [k for k in input().split()]
i, j = int(data[0]), int(data[1])

# стер строки

for stroke in matrix:
    for elem in stroke:
        print(elem, end=' ')
    print()


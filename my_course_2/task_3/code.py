from datetime import datetime as dt

d = {}

for _ in range(int(input())):
	pos = input().split()
	d[pos[2]] = d.get(pos[2], []) + [pos[0] + ' ' + pos[1]]

result = sorted([dt.strptime(i, '%d.%m.%Y') for i in d if len(d[i]) == max(map(lambda x: len(x), d.values()))])

print(*[dt.strftime(i, '%d.%m.%Y') for i in result], sep='\n')
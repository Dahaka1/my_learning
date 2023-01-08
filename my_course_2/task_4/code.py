import csv


def sorting(num):
	with open('../deniro.csv', encoding='utf-8') as file_in:
		lst = list(csv.reader(file_in))
		return sorted(
			[list(map(lambda x: int(x) if i.index(x) == num - 1 and str(x).isdigit() else str(x), i)) for i in lst],
			key=lambda k: k[num - 1])


for j in sorting(int(input())):
	print(*j, sep=',')

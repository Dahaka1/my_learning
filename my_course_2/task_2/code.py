from datetime import datetime as dt

start, end = [dt.strptime(input(), '%d.%m.%Y').toordinal() for i in range(2)]

while (dt.fromordinal(start).day + dt.fromordinal(start).month) % 2 != 1:
	start += 1

lst = [dt.fromordinal(i) for i in range(start, end + 1)]

result = list(filter(lambda x: x.weekday() != 0 and x.weekday() != 3 and lst.index(x) % 3 == 0, lst))

print(*[dt.strftime(i, '%d.%m.%Y') for i in result], sep='\n')




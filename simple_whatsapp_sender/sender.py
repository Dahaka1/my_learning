import csv, webbrowser, time

# В планах сделать полноценную версию (без АПИ вацапа, ибо доступа к нему нет)

with open('ФАЙЛ-Январь-new.csv', encoding='utf-8') as file_in:
	data = list(map(lambda i: i['телефон'] if not ',' in i['телефон'] else None, list(filter(lambda d: d['тренер'] == 'Радашкевич Ярослав', list(csv.DictReader(file_in))))))
	for phone in [i for i in data if i]:
		webbrowser.open_new('https://wa.me/' + '7' + phone[1:])
		time.sleep(3)

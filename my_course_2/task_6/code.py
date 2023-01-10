import csv, \
	json
from datetime import datetime as dt

# ____________________________
# Как еще можно сократить код?
# ____________________________

data, combined_data = sorted(list(csv.reader(open('exam_results.csv')))[1:], key=lambda x: x[2]), {}

for i in data:
	combined_data.setdefault(f'{i[0]}  {i[1]}', []).append(i[2:5])

for student in combined_data:
	combined_data[student] = max(combined_data[student],
								 key=lambda k: (int(k[0]), dt.strptime(k[1], '%Y-%m-%d %H:%M:%S')))

result = sorted([{'name': g.split()[0], 'surname': g.split()[1], 'best_score': int(combined_data[g][0]),
				  'date_and_time': combined_data[g][1], 'email': combined_data[g][2]} for g in combined_data],
				key=lambda item: item['email'])

json.dump(result, open('best_scores.json', 'w'), indent='   ')

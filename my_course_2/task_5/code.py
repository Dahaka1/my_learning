import json
from datetime import datetime as dt

with open('pools.json', encoding='utf-8') as file_in:
	result = max(list(filter(lambda d:
							 dt.strptime(d['WorkingHoursSummer']['Понедельник'].split('-')[0],
										 '%H:%M') <= dt.strptime('10:00', '%H:%M') and
							 dt.strptime(d['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M') >= dt.strptime(
								 '12:00', '%H:%M'),
							 json.load(file_in))),
				 key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
	answer = [print(f"{result['DimensionsSummer']['Length']}x{result['DimensionsSummer']['Width']}"),
			  print(result['Address'])]

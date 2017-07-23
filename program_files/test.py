13153
data = {
	"users": [
		{
		"username": "tim",
		"scores": [323, 33],
		"levels": [3, 1]
		}, 
		{
		"username": "dom",
		"scores": [2100, 2],
		"levels": [5, 7]
		}
	],
	"all_time_score": 12312
}

data_2 = {
	"users": [
		{
		"username": "tim",
		"score": 323,
		"level": 3
		}, 
		{
		"username": "dom",
		"score": 2100,
		"level": 5
		},			{
		"username": "dom",
		"score": 5000,
		"level": 7
		}
	]
}

#for u in data['users']:
	# u['score'] = 12
	#print(u['username'] + ' score = ' + str(u['score']))
'''
for u in data['users']:
	if u['username'] == 'tim':
		u['scores'].append(31)
	# u['score'] = 12
	print(u['username'] + ' score = ' + str(u['scores']))

print(data['users'])

alist = [2, 32, 323, 1, 3]
alist.sort(reverse=True)
print(str(alist))
'''
dicts = []
for user in data_2['users']:
	tmp_list = sorted(data_2['users'], key=lambda k: k['score'], reverse=True)

for item in tmp_list:
	for k,v in item.items():
		print(k,v)
'''
for item in tmp_list:
	for k,v in item.items():
		for score in v:
			try:
				score = int(score)
			except ValueError:
				continue
			scores = {}
			score[item['username']] = {score: item}
			dicts.append(scores)
'''
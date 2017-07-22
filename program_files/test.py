data = {
	"users": [
		{
		"username": "tim",
		"scores": [0, 12]
	}, 
		{
		"username": "dom",
		"scores": [21, 2]
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
import json
def test_1():
	dicts = []
	with open('../data_files/test.json') as file:
		data = json.load(file)
		for user in data['users']:
			user['scores'].sort(reverse=True)
		newlist = sorted(data['users'], key=lambda k: max(k['scores']), reverse=True)

		for item in newlist:
			for k,v in item.items():
				for score in v:
					try:
						score = int(score)
					except ValueError:
						continue
					tmp = {}
					tmp[item['username']] = score
					dicts.append(tmp)

	new_dicts = sorted(dicts, key=lambda k: list(k.values()), reverse=True)
	i = 0
	for d in new_dicts:
		for k,v in d.items():
			if i < 10:
				print(str(i) + ". " + k.title() + "\t.............\t" + str(v))
			i += 1

test_1()
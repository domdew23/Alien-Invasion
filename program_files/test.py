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

for u in data['users']:
	if u['username'] == 'tim':
		u['scores'].append(31)
	# u['score'] = 12
	print(u['username'] + ' score = ' + str(u['scores']))

print(data['users'])
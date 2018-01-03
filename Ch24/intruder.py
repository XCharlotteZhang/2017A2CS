s1='System inactive'
s2='System active'
s3='Alert mode'
s4='Alarm bell ring'
state=s1
halt=False

def judge(inp,sta):
	if inp=='enter pin':
		return s1
	elif inp=='sensor activated':
		if sta==s2:
			return s3
		else:
			return 'invalid'
	elif inp=='2 minutes pass':
		if sta==s3:
			return s4
		else:
			return 'invalid'
	elif inp=='press button':
		if sta==s1:
			return s2
		else:
			return sta
	else:
		return sta

def action(state):
	state=judge(input('input:'),state)
	print(state)

print(state)
while halt==False:
	action(state)

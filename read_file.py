def red(file,tpe='users'):
	# Тут всё понятно
	text=open(file,'r',encoding='UTF-8').readlines()
	user={}
	l='NE_LOL'
	for iq in text:
		i=iq.strip()
		try:
			name=i.split('===')[0]
			pas=i.split('===')[1]
			user[name]=pas
		except:
			l="Ne_lol"
		else:
			l="lol"
	del text
	if l!="lol":
		return None
	elif l=="lol":
		return user




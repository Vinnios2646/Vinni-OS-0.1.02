def python_start_(task31, nn=False):
	# Тут тоже всё сложно, запуск пайтона.
	try: 
		# Пытаемя...
		# Ппайтон = файл который мы кинули в аргументах по типу принт(чтото)||это был энтер)

		ppython=task31
		# Заменяем || на энтер
		ppython=ppython.replace("||","\n")
		# Тут типо того что чуть выше)))
		ppython=ppython.replace("^$^","\t")
		ppython=ppython.replace(" "*4,"\t") # Только тут четыре пробелов (пробел*4)
		# Открываем файл lol.py в папке system в типе ввода как ай
		with open('system/lol.py', 'w', encoding='UTF-8') as i:
			# Очищаем (не знаю зачем, пусть будет)
			i.write("")	
			# Вводим туда наш код
			i.write(ppython)
		# Импортируем путь для импорта файлов
		from sys import path
		# Новая папка для импорта - system
		path.insert(0, "system/")

		# Из папки system импортируем файл lol.py
		import lol
		# Импортируем перезагрузку:)
		from importlib import reload
		# Спрашиваем о рестарте, просто если заново пытаться запустить код, из за того что мы уже импортировали, не чего не будет происходить.
		start=input("Start? (Yes or No)\n").lower() # Делаем высе введённые символы малеьнкими
		if start=="yes":
			# Перезапуск библиотеки
			reload(lol)
		if nn==True:
			try:
				# Если в параметрах мы указали "Истинна" возврощаем функцию из нашего файла
				return lol.edit_py_file()
			except:
				# Не получилось - ошибка
				print("SYSTEM ERROR IN ?")
	except:
		# Если не получилось запустить код - ошибка
		print("SYSTEM ERROR IN START FILE")
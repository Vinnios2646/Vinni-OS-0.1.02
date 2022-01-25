def task():
	
	# Импорт модулей
	from colorama import init
	# Для работы цвета текста на Виндовс
	init()
	from colorama import Fore, Back, Style
	from save_files import sve, open_files
	from time import sleep
	# Импорт файлов
	from random4 import randfloat
	from python_def import python_start_
	# Для остановки работы создаём переменную
	stop=False
	# Открываем файлы
	files=open_files()
	# Открываем первую *папку* в файлах (словарь)
	for i in list(files.keys()):
		if i.split(".")[1]=="folder":
			file_pr=i
			vVv=i
			break
	# Вот и используем переменную
	while stop!=True:
		# Что-то
		li=False
		# Запрашиваем команду добовляя в начале "первую *папку*"
		all__=input(file_pr+"/ ")
		# Задаём параметр функции разделяя строку на пробелы и взяв самый первый индекс
		task=all__.split(" ")[0]
		# Делаем проверки на значение функции
		if task=="new":
			# Создание нового аккаунта из основго cmd файла
			users=open('system/users.tsyst', 'a', encoding='UTF-8') # name===pasword"\n"name===pasword
			usr=input("Your name: ");pas=input("Your password: ")
			users.write(usr+"==="+pas+"\n")
			users.close()
			stop=True
		elif task=="stop":
			# Просто остановка работы
			stop=True
		elif task=="del":
			# Удаляем _все_ аккаунты
			if all__.split(" ")[1]=="all":
				file=open('system/users.tsyst', 'w', encoding='UTF-8')
				file.write("");file.close()
			stop=True
		# elif task=="cd":
		# 	if all__.split(" ")[1] in list(files[file_pr+".folder"]):

		# 	file_pr=file_pr+"/"+str(files[file_pr+".folder"].values())
		elif task=="dir":

			try:
				# Если мы в первой папке, вывести все файлы в первой папке
				text=list(files[file_pr].keys())
			except: 
				# В другом случае код для того что-бы этими значениями была папка в папке в папке в... и так далее
				# Разделяем префикс на части с помощью /
				b=file_pr.split("/")
				# Проходим по длинне префикса
				for i in range(len(b)):
					try:
						# Находим папку в основном файле, присваеваем Зету словарь внутри папки
						z=files[b[i]]
					except:
						# Находим папки внутри папки
						z=z[b[i]]
				# после этого получаем данные файлов в последнем каталоге
				text=list(z.keys())
			# Переменная строка
			abc=""
			# Проходимя по файлам
			for i in text:
				# Добовляем через пробел имя файла
				abc=abc+i+" "
			# Убераем пробелы в конце и начале и заменяем оставшиеся пробелы на " ; "
			abc=abc.strip();abc=abc.replace(" ", " ; ")
			# Выводим файлы в катологе в котором мы находимся в формате файл ; папка ; ещё файл....
			print(abc)
			print("\n")
		elif task=="cd":

			if all__.split(" ")[1]!="..":
				# Если после пробела значение НЕ ".."...
				try:
					# Просто добовляем к префиксу написанный файл
					if all__.split(" ")[1].split(".")[1]=="folder":
						print("Open folder " + all__.split(" ")[1]+"\n")
						file_pr=file_pr+"/"+all__.split(" ")[1]
				except:
					# Не получилось - выводим красную ошибочку, колорама только ради этих ошибок
					for i in range(5):
						print("\033[31m--<System Error | Error #1>--")
						sleep(randfloat(0.003,1.500))
					print("\033[37m\n[R16]")
			else:
				# Если назад в котологе то...
				try:
					# Пытаемся выйти из котолога, это было долго...
					file_pr22 = file_pr.split("/")
					del file_pr22[-1]
					aaa=""
					for i in file_pr22:
						aaa=aaa+"/"+i
					aaa=list(aaa)
					del aaa[0]
					aaa="".join(map(str, aaa))
					# aaa=list(aaa)
					# del aaa[-1]
					# aaa="".join(map(str, aaa))
					print("Open..."+"\n")
					file_pr=aaa
				except:
					# Ошибочка
					for i in range(5):
						print("\033[31m--<System Error | Error #1>--")
						sleep(randfloat(0.003,1.500))
					print("\033[37m\n[R16]")
		# Создание папок
		# ТЕВИИИИИИИИИРП
		# ТЕВИРП
		elif task=="folder-new":
			# Если префикс остался прежним
			if file_pr==vVv:
				# В файлах в словаре префикса создаём словарь с именем которое ввёл пользователь
				files[file_pr][all__.split(" ")[1]+".folder"]={}
			# Тут надо создать как то создание папок в папке.
			else:
				pass
			# 	# name=all__.split(" ")[1]+".folder"
			# 	# Разделяем префикс на части с помощью /
			# 	b=file_pr.split("/")
			# 	# оздаём специальный список
			# 	fls=[]
			# 	# Проходим по длинне префикса
			# 	for i in range(len(b)):
			# 		try:
			# 			# Находим папку в основном файле, присваеваем Зету словарь внутри папки
			# 			z=files[b[i]]
			# 			# print(b[i])
			# 			# print(files)
			# 		except:
			# 			# Находим папки внутри папки
			# 			z=z[b[i]]
			# 			# print(z)
			# 			# print(b[i])
			# 		# Добовляем словарь папок в флс
			# 		print(z)
			# 	for i in fls:
			# 		print(i)
			# 	# print(z)
			# 	# # Заходим в словарь
			# 	# a=files[b[0]]
			# 	# # Удаляем
			# 	# del b[0]
			# 	# # Длинна без первого элемента
			# 	# ln=len(b)
			# 	# # Проходимя по всем элементам
			# 	# for i in range(ln):
			# 	# 	try:
			# 	# 		# В основной папке ищем первую папку после последнего, удалённого значения
			# 	# 		r=a[b[0]]
			# 	# 	except:
			# 	# 		# Не получилось - в самой р ищем первую папку после последней
			# 	# 		r=r[b[0]]
			# 	# 	# Удаляем первое значение
			# 	# 	del b[0]
			# 	# r[name]={"lol.folder":12}
			# # print(z)


		
		elif task=="file-create":
			# Если основной файл
			if file_pr==vVv:
				try: 
					# Данные от пользователя
					task2=all__.split(" ")[1]
					# Тип файлов текстовый
					if task2.split(".")[1]=="txt" or task2.split(".")[1]=="py" or task2.split(".")[1]=="code":
						# Создаем в файлах в словаре префикса файл введнный пользователем - значениие пустое
						files[file_pr][all__.split(" ")[1]]=""
					else:

						# Ошибочка
						for i in range(5):
							print("\033[31m--<System Error | Error #1>--")
							sleep(randfloat(0.003,1.500))
						print("\033[37m\n[R16]")
				except:
					# Ошибочка
					for i in range(5):
						print("\033[31m--<System Error | Error #1>--")
						sleep(randfloat(0.003,1.500))
					print("\033[37m\n[R16]")
			# Тут создание файлов если внутренние папки...


		elif task=="read":
			try:
				# Пытаемся...
				# Таск2 это введённые данные
				task2=all__.split(" ")[1]
				# Если расширение текстовых файлов
				if task2.split(".")[1]=="txt" or task2.split(".")[1]=="py" or task2.split(".")[1]=="code":
					# Заменяем || на новую строку (энтер)
					text=files[file_pr][task2].replace("||","\n")
					# Эти 3 на таб
					text=text.replace("^$^","\t")
					# Четыре пробела так же на таб
					text=text.replace(" "*4,"\t")
					# Выводим данные
					print(text)

			except:
				# Ошибочка
				for i in range(5):
					print("\033[31m--<System Error | Error #1>--")
					sleep(randfloat(0.003,1.500))
				print("\033[37m\n[R16]")
		elif task=="python":

			python_start_(files[file_pr][all__.split(" ")[1]])
		elif task=="save":
			# Сохроняем все файлы в машинных кодах
			sve(files)
		elif task=="file-edit":
			# Из системных файлов файл system_file1.py - это изменение файлов чтобы посмотреть в цмд пиши read system_file1.py
			command_task=python_start_(files[file_pr]["system_file1.py"],nn=True)
			try: 
				try:
					# Пытаемся устоновить значение изменяемого файла на введённые данные
					files[file_pr][all__.split(" ")[1]]=command_task
				except:
					# Ошибка64
					print("64")
			except:
				# Не известная известная ошибка)))
				print("Unknow System Error"*5)
			
			# except:
			# 	# Ошибочка
			# 	for i in range(5):
			# 		print("\033[31m--<System Error | Error #1>--")
			# 		sleep(randfloat(0.003,1.500))
			# 	print("\033[37m\n[R16]")

		# Если команда не распознана
		else:
			# Выводим ошибку
			for i in range(5):
				print("\033[31m--<System Error | Error #1>--")
				sleep(randfloat(0.003,1.500))
			print("\033[37m\n[R16]")
	# Сохраняем все данные
	sve(files)

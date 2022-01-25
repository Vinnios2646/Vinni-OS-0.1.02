def cmd_start():
	# Импорт *библиотек*
	from time import sleep
	from os import mkdir
	# Импорт *файлов*
	from read_file import red
	from cmd_task import task
	from save_files import sve, open_files
	from random4 import randfloat
	# Словарь файлов
	files={}
	# Создаём папку "system" если она не найдена
	try:
		# Создание переменной с хранением всех пользователей
		users=open('system/users.tsyst', 'a', encoding='UTF-8') # name===pasword"\n"name===pasword
		ppthon=open('system/lol.py', 'w', encoding='UTF-8')
		ppthon.close()
	except:
		mkdir('system/')
		users=open('system/users.tsyst', 'a', encoding='UTF-8') # name===pasword"\n"name===pasword
		ppthon=open('system/lol.py', 'w', encoding='UTF-8')
		ppthon.close()
	# Чтение файла
	sr=red('system/users.tsyst')
	# Если в файле не чего нету создавать новый аккаунт
	if sr==None:
		usr=input("Your name: ");pas=input("Your password: ")
		users.write(usr+"==="+pas+"\n")
	# Если аккаунт создан просить данные от него
	else:
		tr=False
		tb=False
		while tb!=True:
			usr=input("User: ")
			if usr in sr.keys():
				tb=True
			else:
				print("Error")
		while tr!=True:
			pas=input("Your password: ")
			if pas==sr[usr]:
				tr=True
			else:
				print("Error") 
	try:
		# Возвращаем из машинных кодов словарь файлов
		files=open_files()
		files["C:.folder"]
	except:
		# Не получилось - создаём стандартные файлы
		files__={
			"C:.folder":{
				"users.folder":{
					"new.folder":{
						"lol.folder":{}
					},
					"lal.folder":{}
				},
				"READ_ME.txt":"Hello!||This is \"VINNI OS\"!||XD",
				"program.py":"print(\"Programm in programm! Print \\\"chelovek\\\" if you want print print. ERRRRRROR MOZGA\")||task=input(\"Command: \")||if task==\"chelovek\":||^$^print(\"Eto ya? LOOOL This is Vinni OS.\\nNo, this is prograaaammmmm in Vinni OS!\")||else:||^$^print(\"Ti ne vvel chelovek...\")||print(\"Ok?\")",
				"system_file1.py":"def edit_py_file():||^$^print(\"Command from System Files! (Path = C:.folder)\\nEdit (HOME64 for stop): \\n\\n\")||^$^all_text=\"\"||^$^text=\"\"||^$^while text!=\"HOME64\":||^$^^$^text=input()||^$^^$^if text!=\"HOME64\":||^$^^$^^$^all_text=all_text+text+\"\".join(map(str, [\"|\",\"|\"])).replace(\"\\t\",\"\".join(map(str, [\"^\",\"$\",\"^\"])))||^$^return all_text"
			}
		}
		# Сохраняем словарь в машинных кодах
		sve(files__)
		# Удаляем словарь для освобождения файлов
		del files__
	# Открываем файлы (Возвращаем из машинных кодов словарь файлов)
	files=open_files()
	print("\tLoading...")
	sleep(randfloat(0.200,2.200));print("\t\tHello "+usr+"!")
	# Включаем работу команд
	task()





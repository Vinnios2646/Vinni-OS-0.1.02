def sve(list):
	# Сложно, но если не знаешь - сложно объяснить, я попытаюсь
	# Импортируем
	from pickle import dump, HIGHEST_PROTOCOL
	# Открываем файл
	with open('system/files.tsyst', 'wb') as f:
		# И сохраняем туда в машинных кодах словарь который приняли
		dump(list, f, HIGHEST_PROTOCOL)
def open_files():
	# Импорт
	from pickle import load as ld
	# Открытие
	with open('system/files.tsyst', 'rb') as f:
		# Перевод словаря с машинных кодов в словарь
		data = ld(f)
	# Возвращаем
	return data
# Надеюсь вы поняли 
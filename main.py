from defs import *
import time

# ====================================== Создание базы если таковая отсутствует

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS "books" (
	"name"	TEXT,
	"author"	TEXT,
	"desc"	TEXT,
	"genre"	TEXT
)
""")

# ====================================== Начало цикла приложения

while True:
	clear()
	menu() # Вызов стартового сообщения со список команд

	action = input("Укажите необходимое действие >>> ")

# ====================================== Добавление книги

	if action == "1":
		clear()
		name   = input("Введите название новой книги >>> ")
		author = input("Введите автора новой книги >>> ")                            # Спрашиваем все данные о книге
		genre  = input("Введите жанр новой книги >>> ")
		desc   = input("Введите краткое описание новой книги >>> ")

		confirm = input("\n\nПроверьте данные выше, и подтвердите добавление новой книги (Y/N) >>> ") # Если человек вдруг ошибся, может отменить и заполнить по новой

		if confirm.lower() == "y":
			add_book(name,author,genre,desc) #Добавление книги
			print("Книга успешно добавлена\nВозврат к меню...")
			time.sleep(2)

		else:
			print("Возврат к меню...")
			time.sleep(2)

# ====================================== Просмотр всего списка книг

	elif action == "2":
		clear()

		books_dict = {} # Создаем словарь для подсчета книг и облегчения использования юзером
		books_list = get_books() # Получаем все доступные книги в базе

		print("Список доступных книг: ")

		for i in range(len(books_list)): # Перебираем все книги и добавляем их в словарь, одновременно выводя в интерфейс
			print(f"{i+1}: {books_list[i][0]} | {books_list[i][1]}")
			books_dict[i+1] = f"{books_list[i][0]} /// {books_list[i][1]}"

		book_to_read = input("Какую книгу прочитаем сегодня? 0 - меню >>> ")

		clear()

		if int(book_to_read) != 0 or book_to_read != "":
			book_to_read = int(book_to_read)
			book_name, book_author = books_dict[book_to_read].split(" /// ")[0], books_dict[book_to_read].split(" /// ")[1]
			book_info = get_book_author_name(book_author,book_name) # Получаем из словаря название книги и его автора для дальнейшего поиска
			book_desc, book_genre = book_info[2],book_info[3]
			print(f"""
Автор: {book_author}
Название: {book_name}
Описание: {book_desc}
Жанр: {book_genre}
				""")

			input("Нажмите Enter для возврата в меню...")

# ====================================== Поиск по жанру

	elif action == "3":
		clear()
		books_dict = {}
		print("Список доступных жанров: ")
		for item in get_genres(): # Получаем список жанров и выводим их юзеру
			print(item)

		genre_find = input("Введите жанр по которому хотите найти книги. 0 - меню >>> ")

		if genre_find != "0":
			clear()
			books_by_genre_list = get_books_by_genre(genre_find) # Список книг по жанру
			print("Список доступных книг: ")
			for i in range(len(books_by_genre_list)):
				print(f"{i+1}: {books_by_genre_list[i][0]} | {books_by_genre_list[i][1]}")
				books_dict[i+1] = f"{books_by_genre_list[i][0]} /// {books_by_genre_list[i][1]}"

			book_to_read = int(input("Какую книгу прочитаем сегодня? >>> "))
			clear()
			book_name, book_author = books_dict[book_to_read].split(" /// ")[0], books_dict[book_to_read].split(" /// ")[1] # Здесь использованы разделители																															# для распознавания автора и наименования 
			book_info = get_book_author_name(book_author,book_name)														    # для распознавания автора и наименования
			book_desc, book_genre = book_info[2],book_info[3]

			print(f"""
Автор: {book_author}
Название: {book_name}
Описание: {book_desc}
Жанр: {book_genre}
				""")
			input("Нажмите Enter для возврата в меню...")

# ====================================== Поиск по ключевому слову

	elif action == "4":
		clear()
		request = input("Введите ключевое слово для поиска по автору/названию книги >>> ")
		clear()
		print("Найденные книги:")
		for item in find_book_like(request): # Список книг по ключ словам
			print(item)
		input("Нажмите Enter для возврата в меню...")

# ====================================== Удаление книги
# Аналогично с поиском книг по всей базе, вместо вывода инфо о книге - удаление

	elif action == "5":
		clear()
		books_dict = {}
		books_list = get_books() 
		print("Список доступных книг: ")
		for i in range(len(books_list)):
			print(f"{i+1}: {books_list[i][0]} | {books_list[i][1]}")
			books_dict[i+1] = f"{books_list[i][0]} /// {books_list[i][1]}"

		book_to_read = int(input("Какую книгу необходимо удалить? 0 - меню >>> "))
		clear()
		book_name, book_author = books_dict[book_to_read].split(" /// ")[0], books_dict[book_to_read].split(" /// ")[1]
		confirm = input("Вы точно хотите удалить эту книгу? (Y/N) >>> ")
		if confirm.lower() == "y":
			delete_book(book_author,book_name)
			clear()
			print("Успешно!")
		elif confirm.lower() == "n":
			input("Удаление отменено. Нажмите Enter для возврата в меню...")


		








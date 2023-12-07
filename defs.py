import os
import sqlite3

def menu(): # Само стартовое сообщение, где описаны действия, доступные пользователю
	print(f"""

===============================================

Добро пожаловать в библиотеку!

Выберите одно из действий:
1 - Добавление новой книги
2 - Просмотреть список всех книг
3 - Просмотреть список книг по запрашиваемому жанру
4 - Поиск книги по автору или названию по ключевому слову
5 - Удаление книги

===============================================

""")

#=============================================================== # Очистка консоли от мусора, дабы пользователь не путался среди выводимых данных

def clear():          
	os.system('cls')

#=============================================================== # Добавление книги по данным пользователя

def add_book(name,author,genre,desc):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"INSERT INTO books VALUES (?,?,?,?)",(name,author,desc,genre))
	con.commit()
	con.close()

#=============================================================== # Получение всего списка книг

def get_books():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"SELECT name,author FROM books")
	return cur.fetchall()
	con.commit()
	con.close()

#=============================================================== # Получение книги по названию+автору

def get_book_author_name(author,name):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"SELECT name,author,desc,genre FROM books WHERE author = ? AND name = ?",(author,name))
	return cur.fetchone()
	con.commit()
	con.close()

#=============================================================== # Получение книг по жанру

def get_books_by_genre(genre):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"SELECT name, author FROM books WHERE genre = ?",(genre,))
	return cur.fetchall()
	con.commit()
	con.close()

#=============================================================== # Получить все жанры добавленные пользователем

def get_genres():
	genres_list = []
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"SELECT genre FROM books")
	for item in cur.fetchall():
		if item[0] not in genres_list:
			genres_list.append(item[0])
	return genres_list
	con.commit()
	con.close()

#=============================================================== # Поиск книг по ключевым словам в авторе и названии

def find_book_like(request):
	books_like_list = []
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"SELECT author, name FROM books WHERE author LIKE '%{request}%'")
	for item in cur.fetchall():
		books_like_list.append(f"{item[0]} | {item[1]}")
	cur.execute(f"SELECT author, name FROM books WHERE name LIKE '%{request}%'")
	for item in cur.fetchall():
		books_like_list.append(f"{item[0]} | {item[1]}")
	return books_like_list
	con.commit()
	con.close()

#=============================================================== # Удаление книги

def delete_book(author,name):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"DELETE FROM books WHERE name = ? AND author = ?",(name,author))
	con.commit()
	con.close()

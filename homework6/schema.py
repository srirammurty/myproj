import sqlite3

connection = sqlite3.connect( 'appdata.db', check_same_thread = False )
cursor = connection.cursor()

cursor.execute(
        """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(32),
        password VARCHAR(16),
        reset_qn VARCHAR(48),
        reset_ans VARCHAR(18),
        is_admin VARCHAR(8)
        );"""
        )
cursor.execute(
        """CREATE TABLE todoList(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(128),
        item VARCHAR(256),
        item_date VARCHAR(16),
        item_status VARCHAR(16)
        );"""
        )
cursor.execute(
        """CREATE TABLE admins(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(32),
        password VARCHAR(16)
        );"""
        )


        
connection.commit()
cursor.close()
connection.close()

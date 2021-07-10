import sqlite3

connection = sqlite3.connect( 'appdata.db', check_same_thread = False )
cursor = connection.cursor()

'''
cursor.execute(
    """
        INSERT INTO users(
            username,
            password,
            reset_qn,
            reset_ans,
            is_admin
            )VALUES(
                'cci@nsg.com',
                'cci',
                'place',
                'srikakulam',
                'YES'
            );
    """
)
cursor.execute(
    """
        INSERT INTO users(
            username,
            password,
            reset_qn,
            reset_ans,
            is_admin
            )VALUES(
                'srm@nsg.com',
                'srm',
                'place',
                'tanuku',
                'YES'
            );
    """
)

cursor.execute(
    """
        INSERT INTO todoList(
            username,
            item,
            item_date,
            item_status
            )VALUES(
                'srm@nsg.com',
                'First Task for SRM',
                '2021/06/25',
                'Pending'
            );
    """
)
'''

cursor.execute(
    """
        INSERT INTO admins(
            username,
            password
            )VALUES(
                'cci@nsg.com',
                'admin'
            );
    """
)
cursor.execute(
    """
        INSERT INTO admins(
            username,
            password
            )VALUES(
                'srm@nsg.com',
                'admin'
            );
    """
)

'''
srm@BANLAP278:/mnt/e/COURSE/Pirple/Fullstack-flask/db_integration$ sudo apt install sqlite3
[sudo] password for srm:
srm@BANLAP278:/mnt/e/COURSE/Pirple/Fullstack-flask/db_integration$ sqlite3 appdata.db
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite> .table
users
sqlite> select * from users;
1|srm|srm|blue
2|cci|cci|green
'''

cursor.execute(
            """SELECT * FROM todoList WHERE username='cci@nsg.com' ORDER BY pk DESC"""
            )
result = cursor.fetchall()
print(result)


connection.commit()
cursor.close()
connection.close()


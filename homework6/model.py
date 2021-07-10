import sqlite3
import datetime

SQL_QUERY = """SELECT {field} FROM {tablename} WHERE username='{username}' ORDER BY pk DESC"""
SQL_QUERY_ITEMS = """SELECT * FROM {tablename} WHERE username='{username}' ORDER BY pk DESC"""
#TABLE_NAME = "users"
TABLE_NAME = "users"
TABLE_NAME_NEW = "usersNew"
TABLE_ITEMS = "todoList"
#"""SELECT favcolor FROM users WHERE username={username} ORDER BY pk DESC""".format(username = user)
def getConnectionAndCursor(db_name='appdata.db'):
    try:
        connection = sqlite3.connect( db_name, check_same_thread = False )
        cursor = connection.cursor()
    except:
        connection = None
        cursor = None
    return connection, cursor
def closeDbConnection(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()

def getColor(user):
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return "cannot determine fav color"
    cursor.execute(
            SQL_QUERY.format(field="favcolor",tablename=TABLE_NAME, username = user)
            )
    color = cursor.fetchone()[0]
    closeDbConnection(connection, cursor)       
    
    return "Favorite color of Mr/Mrs {username} is {color}".format(username = user, color=color)
def getPassword(user):
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return False
    cursor.execute(
            SQL_QUERY.format(field="password",tablename=TABLE_NAME, username = user)
            )
    result = cursor.fetchone()
    closeDbConnection(connection, cursor)
    if( not result ):
        print("User {usr} does not exist in the database".format(usr = user))
        return -1
    return result[0]
def getAdminPassword(user):
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return False
    cursor.execute(
            SQL_QUERY.format(field="password",tablename="admins", username = user)
            )
    result = cursor.fetchone()
    closeDbConnection(connection, cursor)
    if( not result ):
        print("User {usr} does not exist in the database".format(usr = user))
        return -1
    return result[0]
def getAllUsers():
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return False
    cursor.execute(
            "SELECT username from {table_name} ORDER BY pk DESC".format(table_name=TABLE_NAME)
            )
    result = cursor.fetchall()  ## gives result as [ [],  [], [] ]
    db_users = [ usr[0] for usr in result]
    closeDbConnection(connection, cursor)
    return db_users
def getAllAdminUsers():
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return False
    cursor.execute(
            "SELECT username from {table_name} ORDER BY pk DESC".format(table_name='admins')
            )
    result = cursor.fetchall()  ## gives result as [ [],  [], [] ]
    db_admin_users = [ usr[0] for usr in result]
    closeDbConnection(connection, cursor)
    return db_admin_users

def signup(usrname, pw, fc):
    connection, cursor = getConnectionAndCursor()
    ## Check the schema  username VARCHAR(32),password VARCHAR(16),favcolor VARCHAR(16)
    cursor.execute( """INSERT INTO {table_name}(username,password,favcolor)VALUES('{usr}','{pword}','{fcol}');""".format(table_name=TABLE_NAME,usr=usrname,pword=pw, fcol=fc) )
    closeDbConnection(connection, cursor)
    return "Successfully Signedup"

def signupNew(usrname, pw, rq,ra):
    connection, cursor = getConnectionAndCursor()
    ## Check the schema  username VARCHAR(32),password VARCHAR(16),favcolor VARCHAR(16)
    cursor.execute( """INSERT INTO {table_name}(username,password,reset_qn,reset_ans,is_admin)VALUES('{usr}','{pword}','{rq}','{ra}','NO');""".format(table_name=TABLE_NAME,usr=usrname,pword=pw, rq=rq,ra=ra) )
    closeDbConnection(connection, cursor)
    return "Successfully Signedup"
#
def calculateAge(from_date_ymd, today=None,delim="/"):
    if( today == None):
        today = datetime.date.today()
    if( delim not in from_date_ymd):
        print("Wrong date format sent : {0}".format(from_date_ymd))
        return 0
    y,m,d = [ int(x) for x in from_date_ymd.split(delim) ]
    someday = datetime.date(y,m,d)
    diff = someday - today
    return diff.days
def getItems(user):
    items_dict_list = []
    connection, cursor = getConnectionAndCursor()
    if( None  in (connection, cursor) ):
        print("Problem in connecting to database")
        return items_dict_list
    cursor.execute(
            SQL_QUERY_ITEMS.format(field="*",tablename=TABLE_ITEMS, username = user)
            )
    result = cursor.fetchall()
    #[(1, 'srm@nsg.com', 'First Task for SRM', '2021/06/25', 'Pending'),(...)]
    
    if(result):
        items_dict_list = [ {"item":i,"item_date":j,"status":k} for _,_,i,j,k in result ]
    #db_users = [ usr[0] for usr in result]
    closeDbConnection(connection, cursor)
    return items_dict_list
def addItem(user, item):
    today = str(datetime.date.today()).replace("-","/")
    connection, cursor = getConnectionAndCursor()
    ## Check the schema  username VARCHAR(32),password VARCHAR(16),favcolor VARCHAR(16)
    cursor.execute( """INSERT INTO {table_name}(username,item,item_date,item_status)VALUES('{usr}','{item}','{dt}','Pending');""".format(table_name=TABLE_ITEMS,usr=user,item=item, dt=today) )
    closeDbConnection(connection, cursor)
    return "Successfully Signedup"
conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=test;DATABASE=test;UID=user;PWD=password')

myconnection = pyodbc.connect(myconnectionstring, autocommit=True)

mycursor = cnxn.cursor()

cnxn.commit()

cnxn.close()

data_source_name = cnxn.getinfo(pyodbc.SQL_DATA_SOURCE_NAME)

num_products = cnxn.execute("SELECT COUNT(*) FROM product")

cnxn = pyodbc.connect('mydsn')
do_stuff
if not cnxn.autocommit:
    cnxn.commit()  






cursor.execute("select a from tbl where b=? and c=?", (x, y))




for row in cursor.execute("select user_id, user_name from users"):
    print(row.user_id, row.user_name)

row  = cursor.execute("select * from tmp").fetchone()
rows = cursor.execute("select * from tmp").fetchall()

count = cursor.execute("update users set last_logon=? where user_id=?", now, user_id).rowcount
count = cursor.execute("delete from users where user_id=1").rowcount







cursor.execute("select user_name from users where user_id=?", userid)
row = cursor.fetchone()
if row:
    print(row.user_name)




cursor.execute("select user_id, user_name from users where user_id < 100")
rows = cursor.fetchall()
for row in rows:
    print(row.user_id, row.user_name)






for row in cursor.tables():
    print(row.table_name)

# Does table 'x' exist?
if cursor.tables(table='x').fetchone():
   print('yes it does')








# columns in table x
for row in cursor.columns(table='x'):
    print(row.column_name)

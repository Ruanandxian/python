import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
#执行查询语句
cursor.execute('select * from user where id=?',('1',))
#获得查询结果
values=cursor.fetchall()
values
cursor.close()
conn.close()
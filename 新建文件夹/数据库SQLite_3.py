import os,sqlite3
db_file=os.path.join(os.path.dirname(__file__),'123.db')
if os.path.isfile(db_file):
	os.remove(db_file)
#作用是如果存在数据库，就删除重建

conn=sqlite3.connect('123.db')
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20)primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low,high):
	conn=sqlite3.connect('123.db')
	cursor=conn.cursor()
	cursor.execute('select name from user where score>=? and score<=?',(low,high,))
#寻找到的name是tuple
	values=cursor.fetchall()
	print(values)
#打印结果为tuple
# [('Adam',), ('Bart',), ('Lisa',)]
	values=list(map(lambda x:x[0],values))
#map函数使匿名函数作用于每一个tuple上，即取出name，再将结果变为list
#['Adam', 'Bart', 'Lisa']
	print(values)


get_score_in(80, 95)
get_score_in(60, 80)
get_score_in(60, 100)

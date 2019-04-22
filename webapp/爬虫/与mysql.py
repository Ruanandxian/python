import pymysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='1204628226',db='mysql')
cur=conn.cursor()
cur.execute('use scraping')
cur.execute('select * from pages where id=1')
print(cur.fetchall())
cur.close()
conn.close()
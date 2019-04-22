import asyncio,logging
import aiohttp
import aiomysql


def log(sql,args=()):
	#记录sql操作
	logging.info('SQL:%s'%sql)

@asyncio.coroutine
def create_pool(loop,**kw):
	#创建全局连接池，**kw关键字参数集，用于传递host port user password db等的数据库连接参数
	logging.info('create database connection pool...')
	global __pool#定义全局变量
	__pool=yield from aiomysql.creast.pool(
		host=kw.get('host','localhost'),#主机ip，默认本机
		port=kw.get('port',3306),#端口，默认3306
		user=kw['db'],#用户
		password=kw['password'],#用户口令
		db=kw['db'],#选择数据库
		charset=kw.get('charset','utf-8'),#设置数据库编码，默认utf-8
		autocommit=kw.get('autocommit',True),#设置自动提交事物，默认打开
		maxsize=kw.get('maxsize',10),#设置最大连接数，默认10
		minsize=kw.get('minsize',1),#设置最小连接数，默认1
		loop=loop#需要传递一个时间循环实例，若无特别声明，默认使用asyncio。get_event_loop()
		)

@asyncio.coroutine
def select(sql,args,size=None):
	#实现sql语句，select，传入参数分别为sql语句，sql语句中占位符对应的参数集，返回记录行数
	log(sql,args)
	global __pool#使用全局变量_pool
	with (yield from __pool) as conn:
		cur=yield from conn.cursor(aiomysql.DictCursor)
		yield from cur.execute(sql.replace('?','%s'),args or ())
		if size:
			rs=yield from cur.fetchmany()
		else:
			rs=yield from cur.getchall()
		yield from cur.close()
		logging.info('rows returned %s'%len(rs))
		return rs

@asyncio.coroutine
def execute(sql,args):
	log(sql)
	with (yield from __pool) as conn:
		try:
			cur=yield from conn.cursor()
			yield from cur.execute(sql.replace('?','%s'),args)
			affected=cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise
		return affected

def creat_args_string(num):
	#按参数个数制作占位符字符串，用于生成sql语句
	L=[]
	for n in range(num):#sql的占位符是？，num是多少就插入多少个占位符
		L.append('?')
	return ','.join(L)#将L拼接成字符串返回，例如num=3时，“？，？，？”

class Field(object):
	#定义一个数据类型的基类，用于衍生各种在orm中对应数据库的数据类型的类
	def __init__(self,name,column_type,primary_key,default):
		#传入参数对应列名，数据类型，主键，默认值
		self.name=name
		self.column_type=column_type
		self.primary_key=primary_key
		self.default=default
	def __str__(self):
		#print（Field_object)时，返回类名Field，数据类型，列名
		return '<%s, %s:%s>'%(self.__class__.__name__,self.column_type,self.name)

class StringField(Field):
	#从Field继承，定义一个字符类，在orm中对应数据库的字符类型，默认变长100字节
	def __init__(self,name=None,primary_key=False,default=None,ddl='varchar(100)'):
		#可传入参数列名，主键，默认值，数据类型
		super().__init__(name,ddl,primary_key,default)

class BooleanField(Field):
	#从Field继承，定义一个布尔类，在orm中对应数据库的布尔类型
	def __init__(self,name=None,default=False):
		#可传入参数列名，默认值
		super().___init__(name,'boolean',False,default)#对应列名，数据类型，主键，默认值


class IntegerField(Field):
	#从Field继承，定义一个整数类，在orm中对应数据库的bigint整数类型，默认值为0
	def __init__(self,name=None,primary_key=False,default=0):
		#可传入参数列名，主键，默认值
		super().__init__(name,'bigint',primary_key,default)

class FloatField(Field):
	#从Field继承，定义一个浮点数类，在orm中中对应数据库的real双精度fu浮点数类型
	def __init__(self,name=None,primary_key=False,default=0.0):
		super().__init__(name,'real',primary_key,default)

class TextField(Field):
	#从Field继承，定义一个文本类，在orm中对应数据库的text长文本数据类型
	def __init__(self,name=None,default=None):
		super().__init__(name,'text',False,default)
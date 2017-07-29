#-*- coding:utf-8 -*-

#from sqlalchemy import *
#from sqlalchemy.orm import *
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, Unicode, DateTime

engine = create_engine("mysql+pymysql://r7:r7@localhost:3307/dip", echo=True) #创建到数据库的连接,echo=True 表示用logging输出调试结果




from sqlalchemy.sql import table, column, select, update, insert

# define meta information
metadata = MetaData(bind=engine)
mytable = Table('T_COMP_PARAM', metadata, autoload=True)

# select
s = mytable.select() # or:
#s = select([mytable]) # or (if only certain columns):
#s = select([mytable.c.field1, mytable.c.field2, mytable.c.field3])
s = s.where(mytable.param_name == 'db_ip')
result = session.execute(s)
out = result.fetchall()
print(out)
exit(0)

metadata = MetaData(engine) #跟踪表属性


exit(0)

Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

#user_table = Table('T_USER_MANAGER_TEST',
#        metadata,
#        Column('USER_NAME', Unicode(255), primary_key=True),
#        Column('USER_PWD', Unicode(255), unique=True, nullable = False))

user_table = Table('T_USER_MANAGER_TEST', metadata)
#mapper(User, user_table)

u = User()
print(u)
print(metadata)
#metadata.create_all(engine)

#创建了一个自定义了的 Session类
Session = sessionmaker(bind=engine)
#将创建的数据库连接关联到这个session
#Session.configure(bind=engine)
session = Session()
r = session.execute('show databases')
print(list(r))
#session.add_all([
#    User(name='jack'),
#    User(name='mike')
#])
#session.commit()
r = session.query(User).all()
print(r[0].id)


exit(0)
u = User()
#给映射类添加以下必要的属性,因为上面创建表指定这个字段不能为空,且唯一
u.USER_NAME='测试01'.encode('utf-8')
#按照上面创建表的相关代码，这个字段允许为空
u.USER_PWD ='123456'.encode('utf-8')
#在session中添加内容
session.add(u)
#保存数据
session.flush()
#数据库事务的提交,sisson自动过期而不需要关闭
session.commit()

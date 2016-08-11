# python3.5连接mysql数据库,并进行相关操作
import pymysql

# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "101817", "niesheng")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone()方法获取一条数据库。
# data = cursor.fetchone()
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='101817', db='niesheng', charset='UTF8')
# cur = conn.cursor()
# cur.execute("select version()")
# for i in cur:
#     print(i)
# cur.close()
# conn.close()

# 创建数据库表
# db = pymysql.connect("localhost", "root", "101817", "niesheng")
# cursor = db.cursor()  # 使用cursor()方法获取操作游标
# cursor.execute("Drop table if exists Employee")
# sql = """create table Employee (
#          first_name char(20) not null,
#          last_name char(20),
#          age int,
#          sex char(10),
#          income float)"""
# cursor.execute(sql)
# db.close()

# 数据库插入操作
# db = pymysql.connect("localhost", "root", "101817", "niesheng")
# cursor = db.cursor()
# sql = """INSERT INTO Employee(first_name,
#     last_name, age, sex, income)
#     VALUES ('Mac', 'Mohan', 20, 'M', 8000),('Nie', 'Sheng', 26, 'M', 15000)"""
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 数据库查询操作
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据，即全部返回结果
# db = pymysql.connect("localhost", "root", "101817", "niesheng")
# cursor = db.cursor()
# sql = "select * from Employee \
#        where income > '%d'" % (5000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % (fname, lname, age, sex, income))
# except:
#     print("Error:unable to fecth data")
# db.close()

# 数据库更新操作
# db = pymysql.connect("127.0.0.1", "root", "101817", "niesheng")
# cursor = db.cursor()
# sql = "update Employee set age = age+1 where sex = '%c'" % ('M')
# try:
#     cursor.execute(sql)
#     db.commit() # 提交到数据库执行
# except:
#     db.rollback()
# db.close()

# 删除操作
db = pymysql.connect("localhost", "root", "101817", "niesheng")
cursor = db.cursor()
sql = "delete from Employee where age < '%d'" % (22)
try:
    cursor.execute(sql) # 执行SQL
    db.commit() # 提交修改
except:
    db.rollback()
db.close()





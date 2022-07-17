import mysql.connector as conn
#SQL=Structured Query Language

mydb=conn.connect(host="localhost",user="root",passwd="Shrishty@123")
cursor=mydb.cursor()


# cursor.execute("show databases")
# print(cursor.fetchall())

# #Creating New Databases
# cursor.execute("create database wigglewiggle")

# cursor.execute("show databases")
# print(cursor.fetchall())

# q1=cursor.execute("create table wigglewiggle.details(employee_id int(10),employee_name varchar(80), employee_mailid varchar(100),employee_salary int(6),employee_attendance int(3))")

cursor.execute("select * from wigglewiggle.details")
for i in cursor.fetchall():
    print(i)




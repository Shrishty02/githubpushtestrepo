import mysql.connector as conn

mydb =conn.connect(host="localhost", user ="root", password = "Shrishty@123")
print(mydb)
cursor =mydb.cursor()
#cursor.execute("create database sudhanshu")
#cursor.execute("show databases")
s="create table sudhanshu.ineuron(employee_id int(10), emp_name varchar(80), emp_mailid varchar(20), emp_salary int(6),emp_attendence int(3))"
q1 = cursor.execute(s)
q2 =cursor.execute("select * from sudhanshu.ineuron")

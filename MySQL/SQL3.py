import mysql.connector as conn
#SQL=Structured Query Language

mydb=conn.connect(host="localhost",user="root",passwd="Shrishty@123")
cursor=mydb.cursor()

cursor.execute("select employee_id,employee_salary from jigglejiggle.details")

l=[]
for i in cursor.fetchall():
    l.append(i)
    
print(l)
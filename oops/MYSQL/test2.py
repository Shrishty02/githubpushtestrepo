import mysql.connector as conn

mydb =conn.connect(host="localhost", user ="root", password = "Shrishty@123")
print(mydb)
cursor =mydb.cursor()

s="insert into sudhanshu.ineuron values(101, ' sudhanshu kumar','sudh@gmail.com',100,30)"
cursor.excute(s)
mydb.commit()
cursor.execute("select * from sudhanshu.ineuron")
for i in cursor.fetchall():
    print(_i)

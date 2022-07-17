import mysql.connector as conn
#SQL=Structured Query Language

mydb=conn.connect(host="localhost",user="root",passwd="Shrishty@123")
cursor=mydb.cursor()

cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
cursor.execute("insert into jigglejiggle.details values(101 ,'sudhanshu','sudhkumar@mailcom',1000,30) ")
mydb.commit()

cursor.execute("select * from jigglejiggle.details")
print(cursor.fetchall())


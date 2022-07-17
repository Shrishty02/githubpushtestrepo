from select import select
import mysql.connector as conn

mydb =conn.connect(host="localhost", user ="root", password = "Shrishty@123")

cursor =mydb.cursor()
cursor.execute("select )

import mysql.connector as connection
#SQL=Structured Query Language

db=connection.connect(host="localhost",user="root",passwd="Shrishty@123")
cursor=db.cursor()


# cursor.execute("show databases")
# print(cursor.fetchall())

#Creating New Databases
cursor.execute("create database ineuron_database")
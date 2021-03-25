

x=3
y=2
z=x+y
print(z)

print("hello");


import mysql.connector
from mysql.connector import Error

#import MySQLdb

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="accounts")
mycursor = mydb.cursor()
mycursor.execute("select * from account_new1")
#myresult = mycursor.fetchall()
#for x in myresult:
#  print(x);

myresult = mycursor.fetchall()
print(myresult)
myresult = mycursor.fetchone()
print(myresult)
print("Total number of rows is: ", mycursor.rowcount)




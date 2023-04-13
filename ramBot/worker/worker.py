#this will be the worker file to connect all the messages
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="cloud",
  password="cloudroot"
)

print(mydb)

#Get Users
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

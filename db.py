import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)
mycursor = mydb.cursor()

#create
mycursor.execute("create table university (id int , uname varchar(34),score int)")

#insert
uname = input("Enter your  university name")
id = input("Enter your id")
score = input("enter the score")
mycursor.execute("insert into university values(%s,%s,%s)",(id,uname,score))

#update
mycursor.execute("update university set uname ='vig' where id=123 ")

#display
mycursor.execute("select * from university")
uni = mycursor.fetchall()
for clg in uni:
    print(clg)

#name by asc
mycursor.execute("select * from university order by uname desc")
uni = mycursor.fetchall()
for clg in uni:
    print(clg)

#score
mycursor.execute(" select * from university where score > 70 and score < 90 ")
uni = mycursor.fetchall()
for clg in uni:
    #print(clg)

#university name
mycursor.execute(" select uname from university where id=121")
uni = mycursor.fetchall()
for clg in uni:
    print(clg)

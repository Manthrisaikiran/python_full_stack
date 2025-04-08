#importing mysql connector
#connecting database with connector
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manthrisai@3535"
)
# print(mydb)




# #create the databases
# mycursor=mydb.cursor()
# mycursor.execute("create database d2023")

# # checking all the databases
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)



mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manthrisai@3535",
    database="d2023",
)
mycursor=mydb.cursor()



#creating table in databases

# mycursor.execute("create table customer(name varchar(225),address varchar(255))")
# # show tables
# mycursor.execute("show tables")
# for x in mycursor:
#  print(x)




# # #insert in sql
# sql="insert into customer(name,address) values (%s,%s)"
# val=("john","highway 21")
# mycursor.execute(sql,val)

# sql="insert into customer(name,address) values (%s,%s)"
# val=("kiran","highway 20")
# mycursor.execute(sql,val)

# mydb.commit()
# print(mycursor.rowcount,"record inserted.")







# #select in mysql
# mycursor.execute("select * from customer")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)






# # where in mysql
# sql="select*from customer where address='highway 21'"
# mycursor.execute(sql)

# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)





# #delete in mysql
# sql="delete from customer where address='highway 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record(s)deleted")





# #drop
# mycursor=mydb.cursor()
# sql="drop table customer"
# mycursor.execute(sql)





# #update table
# sql="update customer set address = 'canyon 123' where address = 'highway 20'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record(s) affected")






# #truncate
# mycursor=mydb.cursor()
# sql="truncate table customer"
# mycursor.execute(sql)



# # where in mysql
# sql="select*from customer where address='highway 21'"
# mycursor.execute(sql)

# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)
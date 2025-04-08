sql is case-insensitive





C:\Users\sai kiran>mysql -u root -p
Enter password: ***************
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

C:\Users\sai kiran>mysql -u root -p
Enter password: ***************(Manthrisai@3535)
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 8.0.41 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.





file:1_mysql

mysql> source C:\Users\sai kiran\OneDrive\Desktop\mysql\1_mysql.sql
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| student_database   |
| student_table      |
| sys                |
+--------------------+
6 rows in set (0.00 sec)




file:2_data_base


mysql> create database kiran;
Query OK, 1 row affected (0.03 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kiran              |
| mysql              |
| performance_schema |
| student_database   |
| student_table      |
| sys                |
+--------------------+
7 rows in set (0.00 sec)

mysql> use kiran;          # To store database to use
Database changed

mysql> drop database kiran;  #To dope or delete complete table
Query OK, 0 rows affected (0.04 sec)

mysql> show databases;      # to check tables in the database. here kiran database is droped
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| student_database   |
| student_table      |
| sys                |
+--------------------+
6 rows in set (0.00 sec)




mysql> select database();  # to know the which database we have
+------------+
| database() |
+------------+
| NULL       |
+------------+
1 row in set (0.00 sec)



mysql> select database();   # after using the database we will like this by using this command 
+---------------+
| database()    |
+---------------+
| python_course |
+---------------+
1 row in set (0.00 sec)



mysql> show tables in python_course;   #to check how tables are there in py..
Empty set (0.00 sec)




mysql> create table mobile_details
    -> (
    ->     mobile_number int,
    ->     mobile_name varchar(50),
    ->     manufacturing_year int,
    ->     mobile_cost int
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> show tables in python_course;
+-------------------------+
| Tables_in_python_course |
+-------------------------+
| mobile_details          |
+-------------------------+
1 row in set (0.00 sec)


mysql> select * from mobile_details ;
Empty set (0.01 sec)

mysql> show columns in mobile_details;
+--------------------+-------------+------+-----+---------+-------+
| Field              | Type        | Null | Key | Default | Extra |
+--------------------+-------------+------+-----+---------+-------+
| mobile_number      | int         | YES  |     | NULL    |       |
| mobile_name        | varchar(50) | YES  |     | NULL    |       |
| manufacturing_year | int         | YES  |     | NULL    |       |
| mobile_cost        | int         | YES  |     | NULL    |       |
+--------------------+-------------+------+-----+---------+-------+
4 rows in set (0.02 sec)



file:4_ddl_alter

mysql> alter table mobile_details add mobile_color varchar(50);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns in mobile_details;
+--------------------+-------------+------+-----+---------+-------+
| Field              | Type        | Null | Key | Default | Extra |
+--------------------+-------------+------+-----+---------+-------+
| mobile_number      | int         | YES  |     | NULL    |       |
| mobile_name        | varchar(50) | YES  |     | NULL    |       |
| manufacturing_year | int         | YES  |     | NULL    |       |
| mobile_cost        | int         | YES  |     | NULL    |       |
| mobile_color       | varchar(50) | YES  |     | NULL    |       |
+--------------------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)


file:5_ddl_rename

mysql> rename table mobile_details to mobile_records;
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+-------------------------+
| Tables_in_python_course |
+-------------------------+
| mobile_records          |
+-------------------------+
1 row in set (0.00 sec)
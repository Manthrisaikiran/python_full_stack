create table mobile_details
(
    mobile_number int,
    mobile_name varchar(50),
    manufacturing_year int,
    mobile_cost int
);




#cmd output

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
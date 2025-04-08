+---------------+-------------+--------------------+-------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost |
+---------------+-------------+--------------------+-------------+
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
|            11 | apple       |               2020 |       11000 |
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
+---------------+-------------+--------------------+-------------+
5 rows in set (0.00 sec)

mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> savepoint kiran;
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (11,"apple",2020,11000);
Query OK, 1 row affected (0.00 sec)

mysql>
mysql>
mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (12,"one pluse",2020,11000);
Query OK, 1 row affected (0.00 sec)

mysql>
mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (13,"samsang",2020,11000);
Query OK, 1 row affected (0.00 sec)

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost |
+---------------+-------------+--------------------+-------------+
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
|            11 | apple       |               2020 |       11000 |
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
|            11 | apple       |               2020 |       11000 |
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
+---------------+-------------+--------------------+-------------+
8 rows in set (0.00 sec)

mysql> rollback to kiran;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from mobile_records;
+---------------+-------------+--------------------+-------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost |
+---------------+-------------+--------------------+-------------+
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
|            11 | apple       |               2020 |       11000 |
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
+---------------+-------------+--------------------+-------------+
5 rows in set (0.00 sec)
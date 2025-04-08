file:7_dml_insert


mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (11,"two",2020,11000);
Query OK, 1 row affected (0.02 sec)

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | two         |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
1 row in set (0.00 sec)


mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (11,"two",2020,11000);
Query OK, 1 row affected (0.02 sec)

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | two         |               2020 |       11000 | NULL         |
|            11 | two         |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
2 rows in set (0.00 sec)



file:6_ddl_turncate

mysql> truncate table mobile_records;
Query OK, 0 rows affected (0.04 sec)

mysql> select*from mobile_records;
Empty set (0.00 sec)



file:file:7_dml_insert

mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (11,"apple",2020,11000);
Query OK, 1 row affected (0.02 sec)

mysql>
mysql>
mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (12,"one pluse",2020,11000);
Query OK, 1 row affected (0.00 sec)

mysql>
mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (13,"samsang",2020,11000);
Query OK, 1 row affected (0.01 sec)

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | apple       |               2020 |       11000 | NULL         |
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
3 rows in set (0.00 sec)


file:8_dml_update

mysql> update mobile_records set mobile_name="iphone",mobile_cost=50000 where mobile_number=11;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | iphone      |               2020 |       50000 | NULL         |
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
3 rows in set (0.00 sec)


file:9_dml_delete

mysql> delete from mobile_records where mobile_name='iphone';
Query OK, 1 row affected (0.02 sec)

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
2 rows in set (0.00 sec)


file:4_ddl_alter

mysql> alter table mobile_records drop column mobile_color;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost |
+---------------+-------------+--------------------+-------------+
|            12 | one pluse   |               2020 |       11000 |
|            13 | samsang     |               2020 |       11000 |
+---------------+-------------+--------------------+-------------+
2 rows in set (0.00 sec)



file:10_transaction

mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
    -> VALUES (11,"apple",2020,11000);
Query OK, 1 row affected (0.02 sec)

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
+---------------+-------------+--------------------+-------------+
5 rows in set (0.00 sec)

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
INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
VALUES (11,"two",2020,11000);


output:

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



output:


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




INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
VALUES (11,"apple",2020,11000);


INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
VALUES (12,"one pluse",2020,11000);

INSERT INTO mobile_records(mobile_number,mobile_name,manufacturing_year,mobile_cost)
VALUES (13,"samsang",2020,11000);


output:

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
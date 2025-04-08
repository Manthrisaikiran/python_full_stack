update mobile_records set mobile_name="iphone",mobile_cost=50000 where mobile_number=11;


output:

mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | apple       |               2020 |       11000 | NULL         |
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
3 rows in set (0.00 sec)

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
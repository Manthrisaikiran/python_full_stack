truncate table mobile_records;

note: truncate will delete all the rows in table

output:
mysql> select*from mobile_records;
+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | two         |               2020 |       11000 | NULL         |
|            11 | two         |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
2 rows in set (0.00 sec)

mysql> truncate table mobile_records;
Query OK, 0 rows affected (0.04 sec)

mysql> select*from mobile_records;
Empty set (0.00 sec)
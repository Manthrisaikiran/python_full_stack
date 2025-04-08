delete from mobile_records where mobile_name='iphone';

note: delete will delete only select rows in the table.

output:

+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            11 | iphone      |               2020 |       50000 | NULL         |
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
3 rows in set (0.00 sec)

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




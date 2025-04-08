alter table mobile_details add mobile_color varchar(50)
mysql> show columns in mobile_details;





output:
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
5 rows in set (0.00 sec);






alter table mobile_records drop column mobile_color;

output:

+---------------+-------------+--------------------+-------------+--------------+
| mobile_number | mobile_name | manufacturing_year | mobile_cost | mobile_color |
+---------------+-------------+--------------------+-------------+--------------+
|            12 | one pluse   |               2020 |       11000 | NULL         |
|            13 | samsang     |               2020 |       11000 | NULL         |
+---------------+-------------+--------------------+-------------+--------------+
2 rows in set (0.00 sec)

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
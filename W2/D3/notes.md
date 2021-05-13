# SQL Notes

oh CRUD!

1. C -> create
    ```sql
    INSERT INTO db_name.table_name (col_name, col_name) VALUE ("desired_value", "desired_value");
    ```
1. R -> read /retrieve
    ```sql
    SELECT column_name FROM table_name;
    OR
    SELECT * FROM table_name;
    ```
1. U -> update
    ```sql
    UPDATE table_name SET column_name_1 = new_value_1, column_name_2 = new_value_2;
    ```
1. D -> delete
    ```sql 
    DELETE FROM table_name WHERE condition
    ```

---
## Functions

1. concat()
    ```sql
    SELECT CONCAT("Mr. ", first_name, last_name) FROM table_name
    ```

|first_name | last_name |
|-----------|-----------|
| Tyler     | Tbo       |
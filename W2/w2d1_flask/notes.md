# Afternoon 

## Guidelines for mySQL tables

1. Table names are plural and **ALL** lowercase
1. use *"id"* as the primary key - make it auto incremented
1. foreign keys -> refrence table -> singular_id 
    - ie: users (table) orders(table)
    - orders (table) -> foreign key = user_id
1. use created_at and updated_at in **EVERY** Table. 

## Data Types
[Data Types (LP Link)](https://login.codingdojo.com/m/172/7217/52091)
1. VARCHAR()
1. CHAR
1. INT -> 2.1 BILLION
1. BIGINT 
1. TINYINT
1. FLOAT
1. TEXT
1. DATETIME
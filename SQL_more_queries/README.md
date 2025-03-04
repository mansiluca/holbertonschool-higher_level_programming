# SQL - More queries

## Description
This repository contains tasks and exercises focused on advanced SQL querying techniques including permissions, joins, constraints, and subqueries.

## Learning Objectives
By completing this project, you should be able to:

* Create new MySQL users and manage permissions
* Understand and use PRIMARY KEY and FOREIGN KEY constraints
* Use NOT NULL and UNIQUE constraints effectively
* Retrieve data from multiple tables using JOIN operations
* Work with subqueries
* Understand the concepts of UNION and MINUS
* Execute complex queries with various constraints and conditions

## Requirements
* Ubuntu 20.04 LTS
* MySQL 8.0 (version 8.0.25)
* All SQL queries should be executed on MySQL 8.0
* Files must end with a new line
* All SQL files should start with a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE, etc.)

## Resources
* [MySQL Documentation](https://dev.mysql.com/doc/refman/8.0/en/)
* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [SQL technique: joins](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/joins.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

## Usage
Each script can be executed by running:
```
$ cat script_name.sql | mysql -hlocalhost -uroot -p database_name
```

## Tasks
* [Task 0](./0-privileges.sql): Lists privileges of MySQL users
* [Task 1](./1-create_user.sql): Creates a MySQL server user
* [Task 2](./2-create_read_user.sql): Creates a database and user with SELECT privileges
* ... (more tasks to be added)

## Author
* Luca - [GitHub](https://github.com/mansiluca)
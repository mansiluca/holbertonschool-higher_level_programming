# Python - Object-relational mapping

This project connects two amazing worlds: Databases and Python!

In the first part, we use the MySQLdb module to connect to a MySQL database and execute SQL queries.

In the second part, we use the SQLAlchemy Object Relational Mapper (ORM) - an abstraction layer that replaces SQL queries with Python code.

## Learning Objectives

* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

## Requirements

* Python 3.8.5
* MySQLdb version 2.0.x
* SQLAlchemy version 1.4.x
* All files executed with MySQL 8.0
* All files should end with a new line
* All files should be executable

## Installation

```bash
# Install MySQLdb
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo pip3 install mysqlclient

# Install SQLAlchemy
$ sudo pip3 install SQLAlchemy
```

# Install MySQLdb on MacOS
$ brew install mysql
$ pip3 install mysqlclient

# Install SQLAlchemy on MacOS
$ pip3 install SQLAlchemy

## Usage

Examples of basic usage:

```python
# Using MySQLdb
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()

# Using SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine = create_engine('mysql+mysqldb://username:password@localhost/db_name')
session = Session(engine)
```

## Tasks

The project consists of multiple tasks that progressively build understanding of ORM concepts.

## Author
https://github.com/mansiluca/
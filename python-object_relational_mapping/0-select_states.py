#!/usr/bin/python3
def select_states():
    """Select states from database"""
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        username=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

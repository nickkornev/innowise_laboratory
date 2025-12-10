import sqlite3 as sq

with sq.connect("school.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS students")

    cur.execute("DROP TABLE IF EXISTS grades")








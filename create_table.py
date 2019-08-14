# coding: utf8

import sqlite3

conn = sqlite3.connect('test.db')
create_tb = """ CREATE TABLE students(
                name TEXT, addr TEXT, city TEXT, pin TEXT) """
try:
    conn.execute(create_tb)
    print("Table students created successfully;")
except:
    print("数据库连接失败，请检查！")
finally:
    conn.close()
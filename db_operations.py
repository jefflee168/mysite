# coding: utf8

import sqlite3
from flask import Flask,request, render_template, url_for

app = Flask(__name__)

# 数据库插入表单
@app.route('/enternew')
def new_student():
    return render_template('student.html')

# 插入表单数据
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect('test.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students(name,addr,city,pin) VALUES(?,?,?,?)",
                            (name, addr, city, pin))
                conn.commit()
                msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "数据库插入错误！请检查!"
        finally:
            return render_template("results.html", msg=msg)
            conn.close()

@app.route('/')
def list():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("select * from students")
    rows = cursor.fetchall()
    return render_template('list.html', rows=rows)
# coding: utf8

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        results = request.form
        return render_template('results.html', results = results)
    else:
        return "您输入的信息有误，请检查！"
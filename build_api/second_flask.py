#!/usr/bin/python3

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi!\n'

@app.route('/hello/<name>/<int:age>')
def hello_name(name, age):
    return render_template('second_flask.html', username = name, years = age)

if __name__ == '__main__':
    app.run(port=5006)

### the url will be 'http://127.0.0.1:5006/hello/<name>' in a web browser

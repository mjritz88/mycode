#!/usr/bin/python3

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello', methods = ["POST", "GET"])
def hello_world():
    return f'Hello, World!\n'

@app.route('/hello/<name>', methods = ["POST", "GET"])  # note that "GET" is default
def hello_name(name):
    if request.method == "POST":
        nnn = request.form["nm"]
        print(f'nnn={nnn}; this is the alias var for "name"\n')
        return f'Hello, {nnn}!\n'
    else:
        return f'Hello, {name}!\n'

@app.route('/goodbye')
def goodbye_world():
    return f'Goodbye, World!\n'

@app.route('/goodbye/<name>')
def goodbye_name(name):
    return f'Goodbye, {name}!\n'


if __name__ == '__main__':
    app.run(port=1234)

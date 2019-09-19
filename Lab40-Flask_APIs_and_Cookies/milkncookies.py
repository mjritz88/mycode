#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)

# entry point for our users
# renders a template that asks for their name
# index.html points to /setcookie
@app.route("/index")
@app.route("/")
def index():
    return render_template("milkncookies.html")

# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST": # if user sends a POST
        user = request.form["UID"] # set user to value of UID
        fname = request.form["fnm"] # set user to value of fnm
        lname = request.form["lnm"] # set user to value of lnm

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                        #cookievar #value
        resp.set_cookie("userID", user)
        resp.set_cookie("Fname", fname)
        resp.set_cookie("Lname", lname)

        # return our response object includes our cookie
        return resp

    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    UID = request.cookies.get("userID") # preferred method
    fname = request.cookies.get("Fname") # preferred method
    lname = request.cookies.get("Lname") # preferred method

    #print(f'UID={UID}; fname={fname}; lname={lname}\n')
    #print(type(UID))

    if UID == None:
        UID = 'unknown'

    if fname == None:
        fname = 'whoever'

    if lname == None:
        lname = 'you are'

    # UID = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie

    # return HTML embedded with UID (value of userID read from cookie) 
    return f'<h1>Welcome, '+ fname + ' ' + lname + ' (' + UID + ')' + '</h1>'

if __name__ == "__main__":
    app.run(port=5006)

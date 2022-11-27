from flask import Flask, request, render_template, session
from random import randint
from os import getenv

flag = "FMCTF{Str0nG_$3CReTs_4re_M@ndat0ry}"

charset = ['1','2','3','4','5','6','7','8','9','0']
index = randint(0,9)
app = Flask(__name__)
app.secret_key = charset[index]*16
print(app.secret_key)

@app.route("/", methods=["GET"])
def index():
    session["username"] = "impostor"
    session["accessSecret"] = "false"
    secret = "Website is still in developpement, you should come back later ! "
    return render_template("index.html", secret=secret)

@app.route("/SeaCrete", methods=["GET"])
def SeaCrete():
    secret = "Still not admin, you have nothing to do here !"
    if session and session["accessSecret"] == "true":
        secret = "Well done, the flag is "+ flag
    return render_template("index.html", secret=secret)

if __name__ == "__main__":
    app.run()

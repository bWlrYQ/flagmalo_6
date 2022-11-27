from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = "932d669cbe63f11d066cfebbf4b88ca5f763719a"

@app.route("/", methods=["GET"])
def index():
    session["username"] = "Hacker!"
    secret = "Do you think that you can hack my website once again ? Never !"
    return render_template("index.html", secret=secret)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def root():
    year = request.form["year"]
    month = request.form["month"]
    date = request.form["date"]
    hour = request.form["hour"]
    minute = request.form["minute"]
    second = request.form["second"]
    msg = request.form["msg"]
    address = request.form["address"]
    

    


app.run(host="0.0.0.0", port=3000)
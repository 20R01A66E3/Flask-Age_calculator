from flask import Flask, request, render_template
from datetime import date, datetime

# Create a Flask app
app = Flask(__name__)


# Define a route for the default URL
@app.route("/", methods=["GET", "POST"]) # decorator function
def index():
    age = None
    if request.method == "POST":
        birthdate = request.form.get("birthdate")
        age = calculate(birthdate)
    return render_template("index.html", age=age)

# Define age calculator function
def calculate(birthdate):
    try:
        today = date.today()
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


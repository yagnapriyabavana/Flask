from flask import Flask

app=Flask(__name__)

@app.route("/")

def home():
    return "Welcome to dynamic routing api"

@app.route("/student/<name>")
def student(name):
    return f"Welcome {name} to dynamic routing api"

@app.route("/users/<username>")
def users(username):
    return f"Welcome {username} to dynamic routing api"

@app.route("/students/<name>/<branch>/<year>/<course>")
def students(name,branch,year,course):
    return f"Welcome {name} to dynamic routing with multiple parameters api. Your branch is {branch},year is {year} and course is {course}"

@app.route("/students_rolls/<name>/<int:roll_no>/<float:fees>")
def students_rolls(name, roll_no, fees):
    return f"Welcome {name} to dynamic routing with rolls api. Your roll number is {roll_no} and fees is {fees}"

if __name__=="__main__":
    app.run(debug=True)




from flask import *

app = Flask(__name__)
app.secret_key = "123"

@app.route("/success/<name>")
def success(name):
    return "Login successful! Welcome {}".format(name) + ". I am Flask."

@app.route("/failure")
def failure():
    return "Invalid username or password! Please enter the correct username or password."

@app.route("/login", methods = ["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == "abc" and request.form['password'] != "123":
            flash("Invalid password")
            return redirect(url_for("failure"))
        else:
            flash("Login successful")
            return redirect(url_for("success", name = request.form['username']))

if __name__ == "__main__":
    app.run(debug=True)
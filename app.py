from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("welcome.html")

@app.route("/contact")
def Contact():
    return render_template("contact.html")

@app.route("/gallery")
def Gallery():
    return "Gallery Page"

@app.route("/home")
def Home():
    return "Home Page"

if __name__=="__main__":
    app.run()
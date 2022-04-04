from flask import Flask
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my website"

@app.route("/contact")
def Contact():
    return "Contact Page"

@app.route("/gallery")
def Gallery():
    return "Gallery Page"

@app.route("/home")
def Home():
    return "Home Page"

if __name__=="__main__":
    app.run()
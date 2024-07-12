from flask import Flask
import randomname

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/<x>")
def hello_name(x):
    name = randomname.get_name()
    return "Hello, " + name + "!"

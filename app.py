from flask import Flask
import randomname
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/<x>")
def hello_name(x):
    name = r.get(x)
    if not name:
        name = randomname.get_name()
        r.set(x, name)
    return "Hello, " + name + "!"

from flask import Flask
import randomname
import redis

app = Flask(__name__)

redis = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/<x>")
def hello_name(x):
    name = redis.get(x)
    if not name:
        name = randomname.get_name()
        redis.set(x, name)
    return "Hello, " + name + "!"

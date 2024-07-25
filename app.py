from flask import Flask
import randomname
import redis

app = Flask(__name__)

redis = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/names")
def get_all_names_and_addresses():
    keys = redis.keys()
    names_and_addresses = {key: redis.get(key) for key in keys}
    return names_and_addresses

@app.route("/<first_name>")
def hello_name(first_name):
    name = redis.get(first_name)
    if not name:
        name = randomname.get_name()
        redis.set(first_name, name)
    return "Hello, " + name + "!"

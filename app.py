from flask import Flask
import randomname
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('foo', 'bar')
# True
r.get('foo')
# bar

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/<x>")
def hello_name(x):
    name = randomname.get_name()
    return "Hello, " + name + "!"

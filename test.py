import redis

r = redis.Redis(host='localhost', port=6379/tcp, decode_responses=True)

r.set('foo', 'bar')
# True
r.get('foo')
# bar


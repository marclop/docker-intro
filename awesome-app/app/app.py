from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(connection_pool=redis.ConnectionPool(host='redis', port=6379, db=0))


@app.route("/")
def hello():
    return "I said Whale Hello {0} times!".format(r.incr('visits'))


if __name__ == "__main__":
    app.run()

from flask import Flask
from redmbilling.utils.redisutils import redis_db

app = Flask(__name__)

@app.route("/")
def foo_bar():
    return "foo bar"

@app.route("/index")
def index():
    #TODO
    return {"foo":"bar"}

@app.route("/call/<id>")
def call(id):
    redis_db.lpush("consumer",id)
    return id

if __name__ == "__main__":
    app.run()

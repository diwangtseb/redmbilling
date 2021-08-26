import time
from rich import print
from redmbilling.utils.mongoutils import collection
from redmbilling.utils.redisutils import redis_db


def consumer():
    while True:
        id = redis_db.rpop("consumer")
        if id == None:
            time.sleep(10)
        consumer_res = collection.update_one({"token":id},{"$inc":{"count":-1}})
        print(f"{id}'s token -1 {consumer_res}")

if __name__ == "__main__":
    consumer()

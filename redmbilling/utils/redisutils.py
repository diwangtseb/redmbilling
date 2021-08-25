import redis
from redmbilling.config.redis_config import RedisInfo

redis_pool = redis.ConnectionPool(host=RedisInfo.host,port=RedisInfo.port)
redis_db = redis.StrictRedis(connection_pool=redis_pool,decode_responses=True)

if __name__ == "__main__":
    redis_db.set("name","test")

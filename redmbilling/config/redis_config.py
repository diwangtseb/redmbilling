from dataclasses import dataclass

redisInfo = { 
    "host": "localhost", 
    "password": "123456",
    "port": 6379,
    "db": 0
}

@dataclass
class RedisInfo:
    host: str = redisInfo["host"]
    password: str = redisInfo["password"]
    port: int = redisInfo["port"]
    db: int = redisInfo["db"]


if __name__ == "__main__":
    print(RedisInfo)

from dataclasses import dataclass

mongoInfo = {
    "host": "localhost",
    "port": 27017
}

@dataclass
class MongoInfo:
    host: str = mongoInfo["host"]
    port: int = mongoInfo["port"]


if __name__ == "__main__":
    print(MongoInfo)

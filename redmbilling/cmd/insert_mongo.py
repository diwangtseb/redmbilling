from redmbilling.utils.mongoutils import collection
from dataclasses import dataclass

@dataclass
class User:
    token: str
    count: int


def insert_mongo(user:User):
    collection.insert_one({"token":user.token,"count":user.count})


if __name__ == "__main__":
    for index in range(10000):
        user = User(token=str(index),count=10000)
        insert_mongo(user)

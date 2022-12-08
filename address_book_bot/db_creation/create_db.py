from pymongo import MongoClient


def create_db(connection_string: str, db_name: str):

    client = MongoClient(connection_string)
    db = client[db_name]

    return db

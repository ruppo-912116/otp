import logging

from pymongo import MongoClient


def db_instance():
    try:
        client = MongoClient("mongodb://admin:admin@localhost:27017")
        # client = MongoClient("mongodb://localhost:27017")
        client.server_info()  # checking server status and this will throw an exception
        print("connection successful")
        return client.test
    except Exception as e:
        logging.exception(e)

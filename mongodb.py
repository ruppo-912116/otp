import logging

from pymongo import MongoClient


def db_instance():
    try:
        client = MongoClient("mongodb://admin:admin@localhost:27888/?authSource=admin")
        client.server_info()  # checking server status and this will throw an exception
        print("connection successful")
        return client.test
    except Exception as e:
        logging.exception(e)

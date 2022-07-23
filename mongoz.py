from dataclasses import asdict
from distutils.log import debug, info
from itertools import product
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")
format="%(asctime)s - %(levelname)s -%(message)s"
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")
connection_string=f"mongodb+srv://Destrimano1:{password}@test.fun3j30.mongodb.net/?retryWrites=true&w=majority"
client= MongoClient(connection_string)

dbs=client.list_database_names()
print(dbs)
test_db=client.test
collections = test_db.list_collection_names()
print(collections)

def insert_test_doc():
    collection= test_db.test
    test_document={
        "name":"Tim",
        "type":"Test"
    }
    inserted_id=collection.insert_one(test_document).inserted_id
    print(inserted_id)
    insert_test_doc

    production=client.production
    person_collection=production.person_collenction

   


import pymongo
import json
from get_all_data_by_day import get_all_data

def mongodb_conn(conn_str: str):
    try:
        conn = pymongo.MongoClient(conn_str)
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s", e)

    return conn

def update_db(conn_str: str):
    conn = mongodb_conn(conn_str)
    if conn is None:
        # no connection, exit early
        return

    try:
        # print(conn.list_database_names())
        db = conn['bank_currency']
        # print(db.list_collection_names())

        # Get all data today
        get_all_data()

        for bank in db.list_collection_names():
            # # Delete all documents in the "client_addr" collection
            # db[bank].delete_many({})

            # Read the JSON file
            with open(f'server\storage\data\{bank}.json') as f:
                data = json.load(f)

            # Insert the JSON data into the collection
            db[bank].insert_many(data)

    except:
        print("No hosts found")



#if want to run this file to check, please uncomment this following code
username = "csc10008"
pwd = "abcd1234"

connect_str = f"mongodb+srv://{username}:{pwd}@csc10008.tipkf6n.mongodb.net/" # create string to connect to mongdb

update_db(connect_str)


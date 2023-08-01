import pymongo
import json

def mongodb_conn(conn_str: str):
    try:
        conn = pymongo.MongoClient(conn_str)
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s", e)

    return conn

def migrate_data(conn_str: str):
    conn = mongodb_conn(conn_str)
    if conn is None:
        # no connection, exit early
        return

    try:
        print(conn.list_database_names())
        db = conn['socket_client']
        print(db.list_collection_names())

        # Delete all documents in the "client_addr" collection
        db['client_addr'].delete_many({})

        # Read the JSON file
        with open('server\storage\data\client_addr.json') as f:
            data = json.load(f)

        # Insert the JSON data into the collection
        db['client_addr'].insert_many(data)

    except:
        print("No hosts found")



##if want to run this file to check, please uncomment this following code
# username = "csc10008"
# pwd = "abcd1234"

# connect_str = f"mongodb+srv://{username}:{pwd}@csc10008.tipkf6n.mongodb.net/" # create string to connect to mongdb

# migrate_data(connect_str)


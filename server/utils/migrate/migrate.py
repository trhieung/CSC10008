from client_addr_collection import migrate_data as addr_migrate

###
# mongodb+srv://<username>:<password>@csc10008.tipkf6n.mongodb.net/
###

username = "csc10008"
pwd = "abcd1234"

connect_str = f"mongodb+srv://{username}:{pwd}@csc10008.tipkf6n.mongodb.net/" # create string to connect to mongdb

addr_migrate(connect_str)
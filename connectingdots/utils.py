#create a client in the utils file that can be used by any view that wants to interact with MongoDB

from pymongo import MongoClient
# def get_db_handle(db_name, host, port, username, password):
def get_db_handle(db_name):
    host = 'mongodb://127.0.0.1'
    port = 27017
    username = 'rootuser'
    password = 'rootpass'

    client = MongoClient(
        host=host,
        port=int(port),
        username=username,
        password=password
    )
    
    # db_handle = client['db_name']
    # db_handle = client['Companies_db']
    db_handle = client[db_name]

    return db_handle , client
    # return db_handle, client
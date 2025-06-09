from pymongo import MongoClient

host = "localhost"  # e.g., "localhost" or an IP address
port = 27017        # default MongoDB port

# No username or password
connection_string = f"mongodb://{host}:{port}"

# Establish the connection
client = MongoClient(connection_string)

# Access a database
database_name = "aptech"
db = client[database_name]
# Now you can perform operations on the database, e.g.,
db.student.insert_one({"course": "AI-ML"})
#result = db.collection_name.find_one({"key": "value"})
# print(result)

# Remember to close the connection when finished
client.close()
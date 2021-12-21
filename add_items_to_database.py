import json
import pymongo
from datetime import datetime
from catapp.mongodb_config import admin_db, password_db


client = pymongo.MongoClient("mongodb+srv://" + admin_db + ":" + password_db + "@cluster0.ndyoh.mongodb.net/")
data_base_name = "mycats"
collection_name = "items"
database = client[data_base_name]
collection = database[collection_name]
list_items_to_add_database = []
file_to_read = open("data.txt", "r")

for data_json in file_to_read:
    data = json.loads(data_json)
    data_date = data["date"]
    date = datetime.strptime(data_date, "%a %b %d %H:%M:%S %Y")
    data.update({"date": date})
    list_items_to_add_database.append(data)
    
file_to_read.close()

collection.insert_many(list_items_to_add_database)
for item in collection.find():
    print(item)

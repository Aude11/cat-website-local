from pymongo import MongoClient


class DataBase:
    def __init__(self, connection_string="mongodb+srv://admin:password@cluster0.ndyoh.mongodb.net/"):
        #"mongodb://localhost:27017/"
        self.connection_string = connection_string

    def check_data_base(self, data_base_name):  # not in use should be delete
        client = self._connect_client()
        db_list = client.list_database_names()
        if data_base_name in db_list:
            return True
        else:
            return False

    def _connect_to_client(self):
        #return pymongo.MongoClient(self.connection_string)
        return MongoClient(self.connection_string)

    def connect_to_data_base(self, data_base_name):
        client = self._connect_to_client()
        return client[data_base_name]

    def connect_to_collection(self, data_base_name, collection_name):
        data_base = self.connect_to_data_base(data_base_name)
        return data_base[collection_name]

    def drop_collection(self, data_base_name, collection_name):
        collection = self.connect_to_collection(data_base_name,
                                                collection_name)
        collection.drop()

from .DataBase import DataBase


class ModelDB:
    def __init__(self, collection):
        self.collection = collection

    def create_item(self, item_to_add):  
        new_document =  self.collection.insert_one(item_to_add)  
        if type(new_document) == pymongo.results.InsertOneResult:
                return True
        else:
            return None

    def find_all_items(self): 
        all_items = self.collection.find()
        if type(all_items) == pymongo.cursor.Cursor:
            return all_items


    def find_item_filter(self, filter_condition): 
        return self.collection.find(filter_condition)

    def update_item(self, item_to_update, new_value):  
        result = self.collection.update_one(item_to_update, {"$set": new_value})
        is_updated = result.acknowledged
        if is_updated is True:
            return True
        else:
            return None

    def delete_one_item(self, item_to_delete): #not used
        self.collection.delete_one(item_to_delete)

    def delete_all(self): # not used
        self.collection.delete_many({})

    def sort_items(self, fieldname, order): 
        return self.collection.find().sort(fieldname, order)

    def find_last_item_by_fieldname(self, fieldname, order): 
        return self.collection.find().sort(fieldname, order).limit(1)

    def count_items_in_data_base(self):  
        return self.collection.count_documents({})

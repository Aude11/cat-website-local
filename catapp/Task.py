#from bson import ObjectId
from bson.objectid import ObjectId
from collections.abc import Iterable
from .ModelDB import ModelDB
from .SchemaCaturday import SchemaCaturday


class Task:
    def __init__(self, model_data_base, schema):
        self.model_data_base = model_data_base
        self.schema = schema

    def _add_new_document_to_data_base(self):
        query = self.schema.create_new_document()
        if query is not None:
            is_created = self.model_data_base.create_item(query)
            if is_created is True:
                return True
        else:
            return None

    def _get_all_items(self):
        list_items = []
        items = self.model_data_base.find_all_items()
        if isinstance(items, Iterable):
            for item in items:
                list_items.append(item)
            return list_items
        return None

    def _get_number_items(self):
        numbers_item = self.model_data_base.count_items_in_data_base()
        return numbers_item

    def _get_item_by_query(self, key, value):
        query = {key: value} 
        item_object = self.model_data_base.find_item_filter(query)
        for item in item_object:
            return item

    def _get_items_by_date(self):
        items_sorted_by_date = self.model_data_base.sort_items("date", -1)
        list_items = []
        for item in items_sorted_by_date:
            list_items.append(item)
        return list_items

    def _get_last_item_added(self):
        last_item_by_date = self.model_data_base.find_last_item_by_fieldname("date", -1)
        for item in last_item_by_date:
            return item

    def _update_likes(self, result):
        id_item_to_update = self._convert_result_into_ObjectId_format(result)
        item_to_update = self._get_item_by_query("_id", id_item_to_update)
        if item_to_update is not None:
            current_likes = item_to_update["likes"]
            new_like_number = current_likes + 1
            item_to_update = {"_id": id_item_to_update}
            new_value = {"likes": new_like_number}
            is_updated = self.model_data_base.update_item(item_to_update, new_value)
            return is_updated

    def _count_items_in_data_base(self):  # maybe do the checking in app 
        total_items = self.model_data_base.count_items_in_data_base()
        if type(total_items) == int:
            return total_items
        else:
            return None

    def _convert_result_into_ObjectId_format(self, result): 
        if result is not None: # type accpected werkzeug.datastructures.ImmutableMultiDict
            for key, value in result.items():
                    item_to_update = key
            id_item_to_update = ObjectId(item_to_update)
            return id_item_to_update
        else:
            return None

    def notify_update_item_likes(self, result):
        self._update_likes(result)

    def notify_request_create_item(self):
        is_created = self._add_new_document_to_data_base()
        return is_created

    def notify_resquest_get_all_items_from_data_base(self):
        return self._get_items_by_date()

    def notify_resquest_count_items_in_data_base(self):
        return self._get_number_items()

    def notify_resquest_get_last_item_added_to_data_base(self):
        return self._get_last_item_added()

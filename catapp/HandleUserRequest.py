from .Task import Task
from .Factory import Factory


class HandleUserRequest:
    def __init__(self):
        self.task = Factory().set_task()

    def get_last_cat(self):
        last_cat = self.task.notify_resquest_get_last_item_added_to_data_base()
        return last_cat

    def get_cats(self):
        cats = self.task.notify_resquest_get_all_items_from_data_base()
        return cats

    def update_likes(self, result):
        is_updated = self.task.notify_update_item_likes(result)
        return is_updated

    def count_items_data_base(self):
        number = self.task.notify_resquest_count_items_in_data_base()
        return number

    def add_new_item_in_data_base(self):
        self.task.notify_request_create_item()

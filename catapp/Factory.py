from .CatApi import CatApi
from .QuoteZenApi import QuoteZenApi
from .DataBase import DataBase
from .SchemaCaturday import SchemaCaturday
from .ModelDB import ModelDB
from .Task import Task


class Factory:
    def __init__(self):
        self.data_base = DataBase()
        self.cat_api = CatApi()
        self.quote_api = QuoteZenApi()

    def _set_model(self):  
        data_base_name = "mycats"
        collection_name = "items"
        collection = self.data_base.connect_to_collection(data_base_name,
                                                          collection_name)
        model_data_base = ModelDB(collection)
        return model_data_base

    def _set_schema(self):
        schema_caturday = SchemaCaturday(self.cat_api, self.quote_api)
        return schema_caturday

    def set_task(self):
        model_data_base = self._set_model()
        schema = self._set_schema()
        task = Task(model_data_base, schema)
        return task

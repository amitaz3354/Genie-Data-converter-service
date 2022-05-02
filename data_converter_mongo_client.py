from typing import Any

from pymongo import MongoClient

from data_converter_configs import CONNECTION_STRING, DB_NAME, DATA_CONVERTER_COLLECTION
import certifi

class ServiceDbTemplate:

    def __init__(self, collection_name: str):
        self.client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
        self.db = self.client[DB_NAME]
        self.collection = self.db[collection_name]

    def insert(self, document: Any) -> None:
        self.collection.insert_one(document)


class DataConverterDbClient(ServiceDbTemplate):
    def __init__(self):
        super().__init__(collection_name=DATA_CONVERTER_COLLECTION)





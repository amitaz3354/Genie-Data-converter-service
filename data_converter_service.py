import requests

from data_converter_model import DataConverterInput, DataConverterOutput
from data_converter_configs import PDF_TO_TEXT_API_URL, REQUEST_HEADERS
from data_converter_mongo_client import DataConverterDbClient


class DataConverterService:

    def __init__(self, input: DataConverterInput):
        self.input = input
        self.api_url = PDF_TO_TEXT_API_URL
        self.headers = REQUEST_HEADERS
        self.db = DataConverterDbClient()

    def convert(self):
        resp = requests.post(url=self.api_url, headers=self.headers, data=self.input.json())
        self.db.insert(document=resp.json())
        return DataConverterOutput(**resp.json())

    #
    #
    # #todo - will remmove from service
    # @staticmethod
    # def prepare_payload(data: str) -> DataConverterInput:
    #     return DataConverterInput(data)
    #
    # #todo - move it to the UI to handle
    # def encode(self) -> bytes:
    #     return base64.b64encode(self.pdf.read())

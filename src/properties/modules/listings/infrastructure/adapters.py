import json

from src.properties.seedwork.infrastructure.adapters import Adapter


class ListingsAPIAdapter(Adapter):
    def __init__(self):
        self.file_path = "src/properties/modules/listings/infrastructure/mock/data.json"

    def get_properties(self):
        with open(self.file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
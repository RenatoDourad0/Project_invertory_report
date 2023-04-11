from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = path.split(".")[-1]
        if file_type != "json":
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            data = list(json.load(file))
        return data

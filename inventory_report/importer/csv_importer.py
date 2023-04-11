from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = path.split(".")[-1]
        if file_type != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            data = list(csv.DictReader(file))
        return data

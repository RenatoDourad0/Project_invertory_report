from importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = path.split(".")[-1]
        if file_type != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            data = list(csv.DictReader(file))
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)

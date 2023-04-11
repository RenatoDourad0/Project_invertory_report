from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def le_dados(cls, file_type, path):
        data = []
        if file_type == "csv":
            data = CsvImporter.import_data(path)
        if file_type == "json":
            data = JsonImporter.import_data(path)
        if file_type == "xml":
            data = XmlImporter.import_data(path)
        return data

    @classmethod
    def import_data(cls, path: str, type: str):
        file_type = path.split(".")[-1]
        try:
            data = cls.le_dados(file_type, path)
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)
        except Exception as error:
            return error

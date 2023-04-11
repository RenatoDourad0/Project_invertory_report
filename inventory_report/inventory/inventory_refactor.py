from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def le_dados(self, path):
        self.data += self.importer.import_data(path)

    def generate_Report(self, data):
        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)

    def import_data(self, path: str, type: str):
        try:
            data = self.le_dados(path)
            return self.generate_Report(data)
        except ValueError as err:
            raise err
        except Exception as error:
            return error

    def __iter__(self):
        return InventoryIterator(self.data)

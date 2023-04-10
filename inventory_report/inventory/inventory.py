from csv import DictReader
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def gera_relatorio(cls, type, data):
        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def le_xml(cls, path):
        data = []
        myroot = ET.parse(path).getroot()
        for child in myroot:
            report_dict = {}
            for subchild in child:
                report_dict[subchild.tag] = subchild.text
            data.append(report_dict)
        return data

    @classmethod
    def le_dados(cls, file_type, file, path):
        data = []
        if file_type == "csv":
            data = list(DictReader(file))
        if file_type == "json":
            data = list(json.load(file))
        if file_type == "xml":
            data = cls.le_xml(path)
        return data

    @classmethod
    def import_data(cls, path: str, type: str):
        file_type = path.split(".")[-1]
        try:
            with open(path, encoding="utf-8") as file:
                data = cls.le_dados(file_type, file, path)
            return cls.gera_relatorio(type, data)
        except Exception as error:
            return error

from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
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
    def import_data(cls, path):
        file_type = path.split(".")[-1]
        if file_type != "xml":
            raise ValueError("Arquivo inválido")
        data = cls.le_xml(path)
        return data

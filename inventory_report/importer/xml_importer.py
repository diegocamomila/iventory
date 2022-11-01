from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path) as file:
                xmldict = xmltodict.parse(file.read())
                result = xmldict["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
        return result

from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path) as file:
                content = file.read()
                result = json.loads(content)
        else:
            raise ValueError("Arquivo inválido")
        return result

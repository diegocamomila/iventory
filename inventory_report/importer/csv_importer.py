import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                file_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                result = [row for row in file_reader]
        else:
            raise ValueError("Arquivo inválido")
        return result

# obs: material de apoio descrito no arquivo zzzz.md
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
import xmltodict as XmlImporter
import csv as CsvImporter
import json as JsonImporter


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data.extend(self.importer(path))
        if ".csv" in path:
            with open(path, encoding="utf-8") as file:
                report = CsvImporter.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                self.data = list(report)
        if ".xml" in path:
            with open(path) as file:
                report = XmlImporter.parse(file.read())
                self.data = list(report["dataset"]["record"])
        if ".json" in path:
            with open(path) as file:
                report = JsonImporter.load(file)
                self.data = list(report)
        if type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)

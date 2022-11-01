# obs: material de apoio descrito no arquivo zzzz.md
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
import xmltodict as XmlImporter
import csv as CsvImporter
import json as JsonImporter


class InventoryRefactor:
    @classmethod
    def import_data(self, path, type):
        newReport = []
        if ".csv" in path:
            with open(path, encoding="utf-8") as file:
                report = CsvImporter.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                newReport = list(report)
        if ".xml" in path:
            with open(path) as file:
                report = XmlImporter.parse(file.read())
                newReport = list(report["dataset"]["record"])
        if ".json" in path:
            with open(path) as file:
                report = JsonImporter.load(file)
                newReport = list(report)
        if type == "simples":
            return SimpleReport.generate(newReport)
        else:
            return CompleteReport.generate(newReport)

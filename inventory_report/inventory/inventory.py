# obs: material de apoio descrito no arquivo zzzz.md
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict
import csv


class Inventory:
    @classmethod
    def import_data(self, path, type):
        newReport = []
        if ".csv" in path:
            with open(path, encoding="utf-8") as file:
                report = csv.DictReader(file, delimiter=",", quotechar='"')
                newReport = list(report)
        if ".xml" in path:
            with open(path) as file:
                report = xmltodict.parse(file.read())
                newReport = list(report["dataset"]["record"])
        if type == "simples":
            return SimpleReport.generate(newReport)
        else:
            return CompleteReport.generate(newReport)

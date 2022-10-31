# obs: material de apoio descrito no arquivo zzzz.md
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(products: list):
        simple_report = super().generate(products)
        companyName = []
        for product in products:
            companyName.append(product["nome_da_empresa"])
        companyName_stock = "Produtos estocados por empresa:\n"
        companyName = Counter(companyName).most_common()
        for company in companyName:
            companyName_stock += f" {company[0]}: {company[1]}\n"

        return f"{simple_report}\n" f"{companyName_stock}"

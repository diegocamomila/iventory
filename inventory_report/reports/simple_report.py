# obs: material de apoio descrito no arquivo zzzz.md
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products: list):
        manufacturingDate = []
        expirationDate = []
        companyName = []
        for product in products:
            manufacturingDate.append(product["data_de_fabricacao"])
        for product in products:
            expirationDate.append(product["data_de_validade"])
        for product in products:
            companyName.append(product["nome_da_empresa"])

        older_facturingDate = min(manufacturingDate)
        older_expirationDate = min(expirationDate)
        companyName_Products = Counter(companyName).most_common()
        mostProducts_companyName = companyName_Products[0]

        return (
            f"Data de fabricação mais antiga: {older_facturingDate}\n"
            f"Data de validade mais próxima: {older_expirationDate}\n"
            f"Empresa com mais produtos: {mostProducts_companyName[0]}"
        )

from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # Seu teste deve ser escrito aqui
    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    product_report = (
        .format "O produto {product.nome_do_produto}"
        .format " fabricado em {product.data_de_fabricacao}"
        .format " por {product.nome_da_empresa} com validade"
        .format " até {product.data_de_validade}"
        .format " precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    assert str(product) == product_report
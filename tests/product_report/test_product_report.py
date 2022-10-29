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
    assert (
        str(product.__repr__())
        == "O produto Nicotine Polacrilex fabricado em "
        "2021-02-18 por Target Corporation "
        "com validade até 2023-09-17 precisa ser armazenado instrucao 1."
    )

    # product_report = (
    #     f"O produto (string.format{product.nome_do_produto})"
    #     f" fabricado em {product.data_de_fabricacao}"
    #     f" por {product.nome_da_empresa} com validade"
    #     f" até {product.data_de_validade}"
    #     f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    # )

    # assert str(product) == product_report

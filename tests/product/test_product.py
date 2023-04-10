from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        "225",
        "Batedeira",
        "Bend",
        "14/01/1997",
        "14/01/2027",
        "3312312445",
        "n/a",
    )

    assert product.id == "225"
    assert product.nome_do_produto == "Batedeira"
    assert product.nome_da_empresa == "Bend"
    assert product.data_de_fabricacao == "14/01/1997"
    assert product.data_de_validade == "14/01/2027"
    assert product.numero_de_serie == "3312312445"
    assert product.instrucoes_de_armazenamento == "n/a"

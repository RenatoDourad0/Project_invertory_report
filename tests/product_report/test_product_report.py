from inventory_report.inventory.product import Product


def test_relatorio_produto():
    def product():
        p = Product(
            54323,
            "Camisa",
            "RCampos",
            "2020-10-23",
            "2022-10-23",
            "64326473091283",
            "none",
        )
        return p.__repr__()

    def productReturn():
        return (
            "O produto Camisa"
            " fabricado em 2020-10-23"
            " por RCampos com validade"
            " até 2022-10-23"
            " precisa ser armazenado none."
        )

    assert product() == productReturn()

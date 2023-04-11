from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    stock = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": "2",
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
    ]
    report: str = ColoredReport(CompleteReport).generate(stock)
    sequence = report.split(": ")
    print(sequence)
    for elm in [sequence[0], sequence[2], sequence[4]]:
        assert elm.startswith("\x1b[32m")
        assert elm.endswith("\x1b[0m")
    for elm in [sequence[1], sequence[3]]:
        assert elm.startswith("\x1b[36m")
        assert elm.endswith("\x1b[0m")
    assert sequence[-1].startswith("\x1b[31m")
    assert sequence[-1].endswith("\x1b[0m")

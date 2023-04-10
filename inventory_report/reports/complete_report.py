from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list: list[dict]) -> str:
        simpleReport = super().generate(list)
        produtos_por_empresa = {}
        produtos_por_empresa_string = ""
        for elm in list:
            try:
                produtos_por_empresa[elm["nome_da_empresa"]] += 1
            except KeyError:
                produtos_por_empresa[elm["nome_da_empresa"]] = 1
        for elm in produtos_por_empresa:
            produtos_por_empresa_string += (
                f"- {elm}: {produtos_por_empresa.get(elm)}\n"
            )
        return f"""{simpleReport}
Produtos estocados por empresa:
{produtos_por_empresa_string}"""


# stock = [
#     {
#         "data_de_fabricacao": "2023-03-17",
#         "data_de_validade": "2023-05-01",
#         "id": 12,
#         "instrucoes_de_armazenamento": "Dolo...2023-02-15",
#         "data_de_validade": "2023-04-20",
#         "id": 15,
#         "instrucoes_de_armazenamento": "A cum placeat ratione.",
#     }
# ]

# print(CompleteReport.generate(stock))

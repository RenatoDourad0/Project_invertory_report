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

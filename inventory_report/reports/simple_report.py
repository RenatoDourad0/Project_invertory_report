from datetime import date
from dateutil.parser import parse
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list: list[dict]) -> str:
        today = date.today()
        fabricação_mais_antiga = today
        validade_mais_proxima = None
        empresa_mais_produtos = []
        for elm in list:
            fabricacao = parse(
                elm["data_de_fabricacao"].replace("-", "/")
            ).date()
            validade = parse(elm["data_de_validade"].replace("-", "/")).date()
            empresa_mais_produtos.append(elm["nome_da_empresa"])
            if fabricacao < fabricação_mais_antiga:
                fabricação_mais_antiga = fabricacao
            if validade > today and validade_mais_proxima is None:
                validade_mais_proxima = validade
            if validade > today and validade < validade_mais_proxima:
                validade_mais_proxima = validade
        empresa_mais_produtos = Counter(empresa_mais_produtos).most_common(1)[
            0
        ][0]
        return f"""Data de fabricação mais antiga: {fabricação_mais_antiga}
Data de validade mais próxima: {validade_mais_proxima}
Empresa com mais produtos: {empresa_mais_produtos}"""

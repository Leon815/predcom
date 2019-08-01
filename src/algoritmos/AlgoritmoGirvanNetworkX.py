# import girvan_kjahan
from DeteccaoDeComunidadesStrategy import EstrategiaDeDeteccaoDeComunidades

import src.utilidades.girvan_networkx as girvan_networkx


class AlgoritmoGirvan(EstrategiaDeDeteccaoDeComunidades):
    def _executar(self, rede):
        comunidades = girvan_networkx.girvan_newman(rede)
        particionamento = {}
        for comunidade in comunidades:
            i = 0
            for vertice in comunidade:
                particionamento[vertice] = [i]
            i += 1
        return particionamento

    def obter_nome(self):
        return "GirvanNX"
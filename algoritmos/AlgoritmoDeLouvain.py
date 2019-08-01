import community
import networkx as nx
from DeteccaoDeComunidadesStrategy import EstrategiaDeDeteccaoDeComunidades


class AlgoritmoDeLouvain(EstrategiaDeDeteccaoDeComunidades):
    def _executar(self, rede):
        #print(nx.is_directed(rede.grafo_nx))
        #print(type(rede.grafo_nx))

        rede2 = nx.Graph(rede.grafo_nx)
        #print(type(rede2))

        particionamento = community.best_partition(rede2)
        for key in particionamento:
            particionamento[key] = [particionamento[key]]
        return particionamento

    def obter_nome(self):
        return "Louvain"
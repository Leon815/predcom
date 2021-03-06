import utilidades.girvan_newman_kjahan as girvan_newman_kjahan
from DeteccaoDeComunidadesStrategy import EstrategiaDeDeteccaoDeComunidades


class AlgoritmoGirvanKjahan(EstrategiaDeDeteccaoDeComunidades):
    def _executar(self, rede):
        particionamento = {}
        print "Executando Girvan Newman..."
        lista_de_comunidades = girvan_newman_kjahan.executar_Girvan_Newman_Kjahan(rede.grafo_nx.copy())
        print "Obtendo Particionamento..."
        i = 0
        for comunidade in lista_de_comunidades:
            for vertice in comunidade:
                particionamento[vertice] = [i]
            i += 1
        print "Girvan Newman Concluido"
        return particionamento

    def obter_nome(self):
        return "GirvanKjahan"


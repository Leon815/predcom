import sys

class AvaliadorDoExperimento:
    def __init__(self, experimento):
        self.experimento = experimento

    def verificar_previsao_dos_links(self):
        try:
            ranking = self.experimento.ranking_de_pontos
            rede_de_testes = self.experimento.rede_de_testes_core
            self.links_realizados = rede_de_testes.obter_lista_de_links()
            n = len(self.links_realizados)
            self.links_previstos = ranking.obter_n_links_de_pontuacoes_mais_altas(n)
            links_previstos_corretamente = []
            for link in self.links_previstos:
                if link in self.links_realizados:
                    links_previstos_corretamente.append(link)
        except:
            print("Erro na avaliacao do experimento.", sys.exc_info())
            raise
        else:
            return links_previstos_corretamente
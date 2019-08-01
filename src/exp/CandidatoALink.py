import networkx as nx

class CandidatoALink:
    rede = None
    no_a = ''
    no_b = ''
    vizinhos_em_comum = None

    def __init__(self, rede, no_a, no_b):
        self.rede = rede
        self.no_a = no_a
        self.no_b = no_b

    def obter_no_a(self):
        return self.no_a

    def obter_no_b(self):
        return self.no_b

    def obter_vizinhos_de_no_a(self):
        return self.rede.obter_grafo().neighbors(self.no_a)

    def obter_vizinhos_de_no_b(self):
        return self.rede.obter_grafo().neighbors(self.no_b)

    def obter_grau_de_no_a(self):
        return self.rede.obter_grafo().degree(self.no_a)

    def obter_grau_de_no_b(self):
        return self.rede.obter_grafo().degree(self.no_b)

    def obter_vizinhos_em_comum(self):
        if self.vizinhos_em_comum == None:
            self.vizinhos_em_comum = []
            for no in nx.common_neighbors(self.rede.obter_grafo(), self.no_a, self.no_b):
                self.vizinhos_em_comum.append(no)
        return self.vizinhos_em_comum

    def obter_aresta_correspondente(self):
        return (self.no_a, self.no_b)

    #def zerar_parametros_calculados(self):
    #    self.vizinhos_em_comum = None
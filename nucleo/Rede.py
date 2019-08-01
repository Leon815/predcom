import networkx as nx

from utilidades import utils as utils


class Rede:
    def __init__(self, grafo_nx, nome=""):
        self.grafo_nx = grafo_nx
        self.nome = nome
        self.dicionarioDeDados = {}
        self.lista_de_links = []
        #self.lista_de_ouvintes = []

    def obter_nome(self):
        return self.nome

    def zerar_parametros_calculados(self):
        pass

    def obter_ordem(self):
        return self.grafo_nx.order()

    def obter_lista_de_nos(self):
        return self.grafo_nx.nodes()

    def obter_lista_de_vertices(self):
        return self.grafo_nx.nodes()

    def obter_lista_de_links(self):
        #if self.lista_de_links == []:
        #    arestas = self.grafo_nx.edges()
        #    for aresta in arestas:
        #        self.lista_de_links.append(CandidatoALink(self, aresta[0], aresta[1]))
        #return self.lista_de_links
        return self.obter_lista_de_arestas()

    def obter_numero_de_arestas(self):
        return self.grafo_nx.number_of_edges()

    def obter_numero_de_vertices(self):
        return self.obter_ordem()

    def obter_lista_de_links_com_atributos(self):
        #if self.lista_de_links == []:
        #    arestas = self.grafo_nx.edges()
        #    for aresta in arestas:
        #        self.lista_de_links.append(CandidatoALink(self, aresta[0], aresta[1]))
        #return self.lista_de_links
        return self.grafo_nx.edges(data=True)

    def obter_lista_de_arestas(self):
        return list(self.grafo_nx.edges())

    def copia(self):
        return Rede(self.grafo_nx.copy(), self.nome)

    def obter_rede_equivalente_com_link_adicionado(self, link):
        g = self.grafo_nx.copy()
        g.add_edge(*link)
        return Rede(g, self.obter_nome())

    def obter_rede_equivalente_com_links_adicionados(self, lista_de_links):
        nova_rede = self
        for link in lista_de_links:
            nova_rede = nova_rede.obter_rede_equivalente_com_link_adicionado(link)
        return nova_rede

    def obter_rede_equivalente_removendo_link(self, link):
        novo_nome = self.nome + "-" + str(link)
        grafo = self.grafo_nx.copy()
        grafo.remove_edge(*link)
        return Rede(grafo, novo_nome)

    def obter_rede_equivalente_removendo_lista_de_links(self, lista_de_links):
        novo_nome = self.nome + "- links"
        grafo = self.grafo_nx.copy()
        grafo.remove_edges_from(lista_de_links)
        return Rede(grafo, novo_nome)

    def obter_rede_equivalente_removendo_lista_de_vertices(self, lista_de_vertices):
        novo_nome = self.nome + "- vertices"
        grafo = self.grafo_nx.copy()
        grafo.remove_nodes_from(lista_de_vertices)
        return Rede(grafo, novo_nome)

    def obter_rede_equivalente_adicionando_no(self, no):
        novo_nome = self.nome + "+" + str(no)
        grafonx_copia = self.grafo_nx.copy()
        grafonx_copia.add_node(no)
        return Rede(grafonx_copia, novo_nome)

    def obter_rede_equivalente_removendo_no(self, no):
        novo_nome = self.nome + "-" + str(no)
        grafonx_copia = self.grafo_nx.copy()
        grafonx_copia.remove_node(no)
        return Rede(grafonx_copia, novo_nome)

    def obter_rede_equivalente_removendo_lista_de_nos(self, lista):
        novo_nome = self.nome + "- diversos nos"
        grafonx_copia = self.grafo_nx.copy()
        grafonx_copia.remove_nodes_from(lista)
        return Rede(grafonx_copia, novo_nome)

    def obter_grafo(self):
        return self.grafo_nx

    def obter_lista_de_links_nao_presentes(self):
        print("Etapa 1/2")
        arestas = nx.non_edges(self.grafo_nx)

        n = self.grafo_nx.order()
        numero_de_candidatos = (n * (n - 1)/2) - len(self.grafo_nx.edges())

        print("Etapa 2/2")
        lista_de_links = []
        progresso = 0
        for aresta in arestas:
            lista_de_links.append({"no_a": aresta[0], "no_b": aresta[1]})
            utils.apresentar_mensagem_de_progresso(progresso, numero_de_candidatos)
            progresso += 1
        return lista_de_links

    def obter_grafo_complemento(self):
        return Rede(nx.complement(self.grafo_nx))

    def obter_grau_de_no(self, no):
        return self.grafo_nx.degree(no)

    def obter_graus(self):
        return dict(self.grafo_nx.degree())

    def obter_grau_maximo(self):
        graus = sorted(nx.degree(self.grafo_nx).values(), reverse=True)
        dmax = max(graus)
        return dmax

    def excentricidade(self, no):
        return nx.eccentricity(self.grafo_nx, no)

    def contem_link(self, link):
        return self.grafo_nx.has_edge(link[0], link[1])

    def contem_no(self, node):
        return self.grafo_nx.has_node(node)
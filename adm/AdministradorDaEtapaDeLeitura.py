# -*- coding: utf-8 -*-
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from nucleo.LeitorGraphMl import LeitorGraphML
from nucleo.Rede import Rede
import networkx as nx

class AdministradorDaEtapaDeLeitura(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        print("Lendo rede...")
        rede_original = self.ler_rede(self.experimento.parametrizador.caminho_da_rede)
        rede = self.tornar_multigrafo_em_grafo(rede_original)
        self.exibir_mensagem_de_leitura(rede_original, rede)
        self.experimento.administrador_de_dados_do_experimento.atribuir_rede_lida(rede)
        return rede

    def ler_rede(self, caminho):
        return LeitorGraphML().ler_graphml(caminho)

    def remover_multi_arestas(self, rede):
        lista_de_links = rede.obter_lista_de_links()
        lista_de_nos = rede.obter_lista_de_nos()
        nova_rede = Rede(nx.Graph())
        for no in lista_de_nos:
            if not nova_rede.contem_no(no):
                nova_rede = nova_rede.obter_rede_equivalente_adicionando_no(no)
        for link in lista_de_links:
            if not nova_rede.contem_link(link):
                nova_rede = nova_rede.obter_rede_equivalente_com_link_adicionado(link)
        return nova_rede

    def tornar_multigrafo_em_grafo(self, rede):
        grafo_original = rede.grafo_nx
        novo_grafo = nx.Graph(grafo_original)
        return Rede(novo_grafo, rede.obter_nome())

    def exibir_mensagem_de_leitura(self, rede_original, rede):
        print("Rede lida. Número de vertices e arestas: ")
        print("Rede original: ", len(rede_original.obter_lista_de_nos()), rede_original.obter_numero_de_arestas())
        print("Rede convertida: ", len(rede.obter_lista_de_nos()), rede.obter_numero_de_arestas())
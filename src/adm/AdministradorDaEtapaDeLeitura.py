# -*- coding: utf-8 -*-
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from nucleo.LeitorGraphMl import LeitorGraphML
from nucleo.Rede import Rede
import networkx as nx

class AdministradorDaEtapaDeLeitura(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        print("Lendo rede...")
        rede = self.ler_rede(self.experimento.parametrizador.caminho_da_rede)
        print("Rede lida. Número de vertices e arestas: ", len(rede.obter_lista_de_nos()),
              rede.obter_numero_de_arestas())
        self.experimento.administrador_de_dados_do_experimento.atribuir_rede_lida(rede)
        return rede

    def ler_rede(self, caminho):
        return LeitorGraphML().ler_graphml(caminho)


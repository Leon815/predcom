import networkx as nx
from nucleo.Rede import Rede
import os

class LeitorGraphML:
    def ler_graphml(self, caminho_do_arquivo):
        grafonx = nx.read_graphml(caminho_do_arquivo)
        return Rede(grafo_nx=grafonx, nome=os.path.basename(caminho_do_arquivo))

    def escrever_graphml(self, caminho_do_arquivo, grafo):
        nx.write_graphml(grafo, caminho_do_arquivo)
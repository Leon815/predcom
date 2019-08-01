# coding=utf-8
from __future__ import division

import networkx as nx

from utilidades import utils as utils


class CalculadorDeMetricas:
    rede = None
    informacoes_sobre_links = []

    def __init__(self, rede):
        self.rede = rede

    def obter_informacao_sobre_link(self, link):
        return [d for l, d in self.informacoes_sobre_links if l is link][0]

    def acrescentar_informacao_sobre_link(self, link, informacao):
        if link not in self.informacoes_sobre_links:
            self.informacoes_sobre_links.append((link, {}))
        dicionario = [d for l, d in self.informacoes_sobre_links if l is link][0]
        print(dicionario)
        chave, valor = informacao
        dicionario[chave] = valor

    def calcular_vizinhos_em_comum(self, candidato_a_link):
        vizinhos_em_comum = list(nx.common_neighbors(self.rede.grafo_nx, candidato_a_link["no_a"], candidato_a_link["no_b"]))
        candidato_a_link["vizinhos_em_comum"] = vizinhos_em_comum


# Métricas Báse --------------------------------------------------------------------------------------------------------

    # 1. Common Neighbors: |Γ(a) ∩ Γ(b)|
    # O número de vizinhos compartilhados tanto por 'a' quanto por 'b'
    def calcular_metrica_vizinhos_em_comum(self, candidato_a_link):
        if "vizinhos_em_comum" not in candidato_a_link:
            self.calcular_vizinhos_em_comum(candidato_a_link)
        return len(sorted(candidato_a_link["vizinhos_em_comum"]))

    # Jaccard Similarity: |Γ(a) ∩ Γ(b)| / |Γ(a) ∪ Γ(b)|
    # O número de vértices adjacentes tanto a 'a' quanto a 'b',
    # normalizado pelo número de vértices adjacentes ou a 'a', ou a 'b'
    def calcular_metrica_similaridade_de_jaccard(self, candidato_a_link):
        todos_os_vizinhos = utils.mesclar_listas(candidato_a_link["vizinhos_em_comum"], candidato_a_link["vizinhos_em_comum"])
        return len(candidato_a_link["vizinhos_em_comum"]) / len(todos_os_vizinhos)

    # Similaridade de Sorensen: | Γ(a)∩Γ(b) | / d(a) + d(b)
    # O número de vértices adjacentes tanto a 'a' quanto a 'b',
    # normalizado pela soma dos graus de 'a' e de 'b'.
    def calcular_similaridade_de_sorensen(self, candidato_a_link):
        soma = candidato_a_link["grau_de_no_a"] + candidato_a_link["grau_de_no_b"]
        return len(candidato_a_link["vizinhos_em_comum"]) / soma

    # Resource Allocation: With c∈ Γ(a)∩Γ(b), Σ 1/d(c)
    # The sum of the inverses of the degrees of vertices
    # adjacent to both a and b.
    def calcular_alocacao_de_recursos(self, candidato_a_link):
        vizinhos_em_comum = candidato_a_link["vizinhos_em_comum"]
        pontos = 0
        for no in vizinhos_em_comum:
            pontos += 1 / self.rede.obter_grafo().degree(no)
        return pontos

    # Leicht-Holme-Newman: |Γ(a)∩Γ(b)| / d(a)×d(b)
    # The number of vertices adjacent to both a and b
    # normalized by the product of the degrees of a and b
    def calcular_Leicht_Holme_Newman(self, candidato_a_link):
        produto = candidato_a_link["grau_de_no_a"] * candidato_a_link["grau_de_no_b"]
        return len(candidato_a_link["vizinhos_em_comum"]) / produto

# Métricas Estendidas ---------------------------------------------------------------------------------------------------

    # Common Neighbors 1 (CN1): In this measure, CN1(a, b)
    # begins with the base score given by CN(a, b), and then
    # for every neighbor i shared by a and b, CN1(a, b) receives
    # an additional point for every community that a,
    # b, and i are all in.
    def calcular_metrica_vizinhos_em_comum_1(self, candidato_a_link, comunidades_por_no):
        cn = self.calcular_metrica_vizinhos_em_comum(candidato_a_link)
        no_a = candidato_a_link["no_a"]
        no_b = candidato_a_link["no_b"]
        pontos = 0
        for no_em_comum in candidato_a_link["vizinhos_em_comum"]:
            for comunidades in comunidades_por_no[no_em_comum]: #DETCOM
                if comunidades in comunidades_por_no[no_a] and comunidades in comunidades_por_no[no_b]: #DETCOM
                #if comunidades_por_no[no_em_comum] == comunidades_por_no[no_a] == comunidades_por_no[no_b]: #LOUVAIN
                    pontos += 1
        return cn + pontos

    def calcular_metrica_vizinhos_em_comum_2(self, candidato_a_link, particionamento):
        cn = self.calcular_metrica_vizinhos_em_comum(candidato_a_link)
        no_a = candidato_a_link["no_a"]
        no_b = candidato_a_link["no_b"]
        pontos = 0
        for no_em_comum  in candidato_a_link["vizinhos_em_comum"]:
            if particionamento[no_em_comum] == particionamento[no_a]  == particionamento[no_b]:
                pontos += 1
        return cn + pontos




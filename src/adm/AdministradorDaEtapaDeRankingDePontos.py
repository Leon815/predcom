# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from exp.RankingDePontos import RankingDePontos

class AdministradorDaEtapaDeRankingDePontos(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        self.ranking_de_pontos = RankingDePontos(self.experimento.rede_de_treino_core, self.experimento.particionamento_de_comunidades)
        print("Calculando Pontuacoes...")
        self.ranking_de_pontos.calcular_pontuacao_dos_links(self.experimento.candidatos_a_link)
        return self.ranking_de_pontos

# -*- coding: utf-8 -*-
import networkx as nx
from datetime import datetime
import utilidades.utils as utils

from exp.AdministradorDeDadosDoExperimento import AdministradorDeDadosDoExperimento
from adm.AdministradorDaEtapaDeLeitura import AdministradorDaEtapaDeLeitura
from adm.AdministradorDaEtapaDeParticionamento import AdministradorDaEtapaDeParticionamento
from adm.AdministradorDaEtapaDeCorteCore import AdministradorDaEtapaDeCorteCore
from adm.AdministradorDaEtapaDeIdentificarCandidatosALink import AdministradorDaEtapaDeIdentificarCandidatosALink
from adm.AdministradorDaEtapaDeDeteccaoDeComunidades import AdministradorDaEtapaDeDeteccaoDeComunidades
from adm.AdministradorDaEtapaDeRankingDePontos import AdministradorDaEtapaDeRankingDePontos
from adm.AdministradorDaEtapaDeAvaliacaoDeLinks import AdministradorDaEtapaDeAvaliacaoDeLinks
from adm.AdministradorDaEtapaDeEscritaDeInformacoes import AdministradorDaEtapaDeEscritaDeInformacoes
from EscritorDeInformacoesDoExperimento import EscritorDeInformacoesDoExperimento


class Experimento():
    def __init__(self, parametrizador):
        self.parametrizador = parametrizador
        self._inicializar_objetos_principais()

    def _inicializar_objetos_principais(self):
        self.administrador_de_dados_do_experimento = AdministradorDeDadosDoExperimento()        
        self.administrador_de_dados_do_experimento.atribuir_data_e_hora_de_inicio_do_experimento(utils.momento())
    
    def executar(self):
        self._efetuar_etapa_de_leitura_da_rede()                    #ETAPA 1
        self._efetuar_etapa_de_separacao_entre_treino_e_teste()     #ETAPA 2
        self._efetuar_etapa_de_corte_core()                         #ETAPA 3
        self._efetuar_etapa_de_idetificar_candidatos_a_link()       #ETAPA 4
        self._efetuar_etapa_de_deteccao_de_comunidades()            #ETAPA 5
        self._efetuar_etapa_de_ranking_de_pontos()                  #ETAPA 6
        self._efetuar_etapa_de_avaliacao_de_links()                 #ETAPA 7
        return self.administrador_de_dados_do_experimento

    #Etapa 1
    def _efetuar_etapa_de_leitura_da_rede(self):
        self.administrador_de_dados_do_experimento.atribuir_data_e_hora_de_fim_do_experimento(utils.momento())
        self.rede = AdministradorDaEtapaDeLeitura(self).executar_etapa()

    #Etapa 2
    def _efetuar_etapa_de_separacao_entre_treino_e_teste(self):
        self.rede_de_treino, self.rede_de_testes = AdministradorDaEtapaDeParticionamento(self).executar_etapa()

    #Etapa 3
    def _efetuar_etapa_de_corte_core(self):
        self.rede_de_treino_core, self.rede_de_testes_core = AdministradorDaEtapaDeCorteCore(self).executar_etapa()

    # Etapa 4
    def _efetuar_etapa_de_idetificar_candidatos_a_link(self):
        self.candidatos_a_link = AdministradorDaEtapaDeIdentificarCandidatosALink(self).executar_etapa()

    # Etapa 5
    def _efetuar_etapa_de_deteccao_de_comunidades(self):
        self.particionamento_de_comunidades = AdministradorDaEtapaDeDeteccaoDeComunidades(self).executar_etapa()

    # Etapa 6
    def _efetuar_etapa_de_ranking_de_pontos(self):
        self.ranking_de_pontos = AdministradorDaEtapaDeRankingDePontos(self).executar_etapa()

    # Etapa 7
    def _efetuar_etapa_de_avaliacao_de_links(self):
        self.links_previstos_corretamente = AdministradorDaEtapaDeAvaliacaoDeLinks(self).executar_etapa()
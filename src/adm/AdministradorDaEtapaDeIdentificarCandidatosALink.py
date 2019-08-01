# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato

class AdministradorDaEtapaDeIdentificarCandidatosALink(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        print("Identificando candidatos a link...")
        candidatos_a_link = self.obter_candidatos_a_link(self.experimento.rede_de_treino_core)
        if len(candidatos_a_link) == 0:
            print("Nao existem candidatos a link")
        self.experimento.administrador_de_dados_do_experimento.atribuir_candidatos_a_link(candidatos_a_link)
        return candidatos_a_link

    def obter_candidatos_a_link(self, rede):
        return rede.obter_lista_de_links_nao_presentes()
# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from exp.EscritorDeInformacoesDoExperimento import EscritorDeInformacoesDoExperimento

class AdministradorDaEtapaDeEscritaDeInformacoes(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        self.escrever_informacoes_da_execucao()

    def escrever_informacoes_da_execucao(self):
        EscritorDeInformacoesDoExperimento(self.experimento).escrever_dados_do_experimento()
        pass
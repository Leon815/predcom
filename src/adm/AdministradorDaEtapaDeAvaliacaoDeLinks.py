# -*- coding: utf-8 -*-
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from exp.AvaliadorDoExperimento import AvaliadorDoExperimento

class AdministradorDaEtapaDeAvaliacaoDeLinks(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        avaliador = AvaliadorDoExperimento(self.experimento)
        self.links_previstos_corretamente = avaliador.verificar_previsao_dos_links()
        self.links_previstos = avaliador.links_previstos
        self.links_realizados = avaliador.links_realizados
        self.registrar_informacoes()
        print("Acertos: " + str(len(self.links_previstos_corretamente)) + " de " + str(len(self.experimento.rede_de_testes_core.obter_lista_de_arestas())) + " links.")
        return self.links_previstos_corretamente

    def registrar_informacoes(self):
        adm = self.experimento.administrador_de_dados_do_experimento
        adm.atribuir_links_previstos(self.links_previstos)
        adm.atribuir_links_previstos_corretamente(self.links_previstos_corretamente)
        adm.atribuir_links_realizados(self.links_realizados)
        adm.atribuir_numero_de_acertos(len(self.links_previstos_corretamente))
        adm.atribuir_numero_de_erros(len(self.links_previstos) - len(self.links_previstos_corretamente))
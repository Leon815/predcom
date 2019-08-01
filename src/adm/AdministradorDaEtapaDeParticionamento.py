# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from exp.ParticionadorDeRede import ParticionadorDeRede

class AdministradorDaEtapaDeParticionamento(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        print("Separando rede entre treino e teste...")
        rede_de_treino, rede_de_testes = self._separar_rede_entre_treino_e_teste()
        self._exibir_mensagem_de_numero_de_arestas(rede_de_treino, rede_de_testes)
        self.registrar_dados_da_execucao(rede_de_treino, rede_de_testes)
        return rede_de_treino, rede_de_testes

    def _separar_rede_entre_treino_e_teste(self):
        particionador = ParticionadorDeRede()
        parametrizador = self.experimento.parametrizador
        if parametrizador.avaliacao_por_kold:
            rede_de_treino, rede_de_testes = particionador.separar_rede_por_kfold(self.experimento.rede,
                                                                                       int(parametrizador.etapa),
                                                                                       int(parametrizador.quantidade_de_etapas))
        else:
            periodo_de_treino, periodo_de_teste = parametrizador.periodo_de_treino, parametrizador.periodo_de_testes
            rede_de_treino, rede_de_testes = particionador.separar_rede_por_periodo(self.experimento.rede,
                                                                                    periodo_de_treino=periodo_de_treino,
                                                                                    periodo_de_testes=periodo_de_teste,
                                                                                    palavra_chave_que_identifica_ano = parametrizador.palavra_para_ano_na_rede,
                                                                                    caminho_da_rede=parametrizador.caminho_da_rede)
        return rede_de_treino, rede_de_testes

    def _exibir_mensagem_de_numero_de_arestas(self, rede_de_treino, rede_de_testes):
        print("Número de arestas em rede de treino e rede de testes: ")
        print(rede_de_treino.obter_numero_de_arestas(), rede_de_testes.obter_numero_de_arestas())

    def registrar_dados_da_execucao(self, rede_de_treino, rede_de_testes):
        administrador_de_dados = self.experimento.administrador_de_dados_do_experimento
        administrador_de_dados.atribuir_redes_de_treino_e_teste(rede_de_treino, rede_de_testes)
import os
from nucleo.LeitorGraphMl import LeitorGraphML
import utilidades.utils as utils

class EscritorDeInformacoesDoExperimento:
    def __init__(self, experimento):
        self.experimento = experimento

    def escrever_dados_do_experimento(self, experimento):
        self.parametrizador, self.administrador_de_dados = experimento.parametrizador, experimento.administrador_de_dados_do_experimento
        diretorio_de_resultados_base = self.criar_diretorio_de_resultados_base()

        if self.parametrizador.avaliacao_por_kold:
            self._criar_diretorio_de_resultados_kfold()

        diretorio_por_etapa = self.criar_diretorio_de_arquivos_de_resultados(diretorio_de_resultados_base)
        self.arquivo_de_resultados = self.criar_arquivo_de_resultados

    def criar_diretorio_de_resultados_base(self):
        self.nome_base, _ = os.path.splitext(self.experimento.rede.nome)
        diretorio_base = '../resultados/' + self.nome_base
        return diretorio_base

    def criar_diretorio_de_resultados_kfold(self):
        pass

    def criar_diretorio_de_arquivos_de_resultados(self, diretorio_base):
        data_e_hora_da_execucao = self.administrador_de_dados.data_e_hora_de_inicio
        if self.parametrizador.avaliacao_por_kold:
            etapa = self.parametrizador.etapa
            diretorio_de_resultados = diretorio_base + "/Fold " + str(etapa)
        else:
            inicio_treino, fim_treino = self.parametrizador.periodo_de_treino
            inicio_testes, fim_testes = self.parametrizador.periodo_de_testes
            nome_da_pasta = "TREINO " + str(inicio_treino) + " - " + str(fim_treino) + \
                            "TESTES " + str(inicio_testes) + " - " + str(fim_testes)
            utils.criar_diretorio_se_nao_existir(diretorio_base)
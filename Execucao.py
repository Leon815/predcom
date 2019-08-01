from exp.Parametrizador import Parametrizador
from exp.Experimento import Experimento
from exp.BancoDeDadosDaExecucao import BancoDeDadosDaExecucao
from exp.EscritorDeDadosDaExecucaoPorPeriodo import EscritorDeDadosDaExecucaoPorPeriodo
from exp.EscritorDeDadosDaExecucaoPorKFold import EscritorDeDadosDaExecucaoPorKFold
import os

class Execucao():
    def __init__(self, arquivo_de_parametros):
        self.parametrizador = Parametrizador(arquivo_de_parametros)
        self.banco_de_dados_da_execucao = BancoDeDadosDaExecucao(self.parametrizador)

    def executar(self):
        self.inicializar_banco_de_dados_da_execucao()
        if self.parametrizador.avaliacao_por_periodo:
            administrador_de_dados_do_experimento = Experimento(self.parametrizador).executar()
            self.banco_de_dados_da_execucao.adicionar_administrador_de_dados_de_experimento(administrador_de_dados_do_experimento)
            escritor_de_dados = EscritorDeDadosDaExecucaoPorPeriodo(self.banco_de_dados_da_execucao)

        else:
            for etapa in range(1, self.parametrizador.quantidade_de_etapas + 1):
                self.parametrizador.etapa = etapa
                administrador_de_dados_do_fold = Experimento(self.parametrizador).executar()
                self.banco_de_dados_da_execucao.adicionar_administrador_de_dados_de_experimento(administrador_de_dados_do_fold)
            escritor_de_dados = EscritorDeDadosDaExecucaoPorKFold(self.banco_de_dados_da_execucao)
        escritor_de_dados.escrever_resultados()

    def inicializar_banco_de_dados_da_execucao(self):
        nome_da_rede, _ = os.path.splitext(os.path.basename(self.parametrizador.caminho_da_rede))
        self.banco_de_dados_da_execucao.atribuir_nome_da_rede(nome_da_rede)
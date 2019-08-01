import abc

class EscritorDeDadosDaExecucao():
    __metaclass__ = abc.ABCMeta

    def __init__(self, banco_de_dados_da_execucao):
        self.banco_de_dados_da_execucao = banco_de_dados_da_execucao
        self.administrador_de_dados_do_experimento = banco_de_dados_da_execucao.bancos_de_dados_de_experimentos[0]
        self.parametrizador = self.banco_de_dados_da_execucao.parametrizador

    def escrever_resultados(self):
        self.diretorio_de_resultados = self.criar_diretorio_de_resultados()
        self.escrever_arquivo_de_configuracoes(self.diretorio_de_resultados, self.parametrizador.arquivo_de_parametros)
        self.escrever_arquivo_de_resultados(self.diretorio_de_resultados)
        self.escrever_informacoes_das_redes()
        self.escrever_arquivo_de_core("core.txt")



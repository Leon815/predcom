from EscritorDeInformacoesDoExperimento import EscritorDeInformacoesDoExperimento

class BancoDeDadosDaExecucao():
    def __init__(self, parametrizador):
        self.bancos_de_dados_de_experimentos = []
        self.parametrizador = parametrizador

    def adicionar_administrador_de_dados_de_experimento(self, admnistrador_de_dados_do_experimento):
        self.bancos_de_dados_de_experimentos.append(admnistrador_de_dados_do_experimento)

    def obter_nome_da_rede(self):
        return self.nome_da_rede

    def atribuir_nome_da_rede(self, nome_da_rede):
        self.nome_da_rede = nome_da_rede
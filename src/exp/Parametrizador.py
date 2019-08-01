class Parametrizador():
    def __init__(self, arquivo_de_parametros):
        self.arquivo_de_parametros = arquivo_de_parametros
        for linha in arquivo_de_parametros:
            if linha[0] == '#' or linha[0] == '\n':
                continue
            parametro, valor = self._avaliar_linha(linha)
            self._atribuir_valor_de_parametro(parametro, valor)
        self._inicializar_parametros_adicionais()

    def _avaliar_linha(self, linha):
        parametro, valor = linha.split(": ")
        return (parametro.strip(), valor.strip())


    def _atribuir_valor_de_parametro(self, parametro, valor):
        if parametro == "Caminho da Rede":
            self.caminho_da_rede = valor
        elif parametro == "Estrategia":
            self.estrategia_de_deteccao = valor
        elif parametro == "Avaliacao por KFold":
            self.avaliacao_por_kold = (valor == 'S')
            self.avaliacao_por_periodo = not self.avaliacao_por_kold
        elif parametro == "Periodo de Treino":
            self.periodo_de_treino = eval(valor.strip())
        elif parametro == "Periodo de Testes":
            self.periodo_de_testes = eval(valor.strip())
        elif parametro == "Parametro Core Treino":
            self.pcore_treino = int(valor)
        elif parametro == "Parametro Core Testes":
            self.pcore_testes = int(valor)
        elif parametro == "Quantidade de Etapas (K)":
            self.quantidade_de_etapas = int(valor)
        elif parametro == "Palavra-Chave Ano":
            self.palavra_para_ano_na_rede = valor

    def _inicializar_parametros_adicionais(self):
        self.etapa = -1
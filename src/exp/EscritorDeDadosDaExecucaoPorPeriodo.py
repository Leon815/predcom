import os
import src.utilidades.utils as utils

class EscritorDeDadosDaExecucaoPorPeriodo():
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

    def criar_diretorio_de_resultados(self):
        nome_da_rede = self.banco_de_dados_da_execucao.obter_nome_da_rede()
        nome_da_pasta = self.montar_nome_da_pasta()
        diretorio_principal = "../resultados/periodo/" + nome_da_rede + "/" + nome_da_pasta
        utils.criar_diretorio_se_nao_existir(diretorio_principal)
        return diretorio_principal

    def montar_nome_da_pasta(self):
        inicio_treino, fim_treino = self.parametrizador.periodo_de_treino
        inicio_testes, fim_testes = self.parametrizador.periodo_de_testes
        nome_da_pasta = str(inicio_treino) + "-" + str(fim_treino) + \
                        ": " + str(inicio_testes) + "-" + str(fim_testes)
        return nome_da_pasta

    def escrever_arquivo_de_configuracoes(self, diretorio_de_resultados, arquivo_de_configuracoes):
        utils.criar_diretorio_se_nao_existir(diretorio_de_resultados)
        arquivo = open(diretorio_de_resultados + "/config.txt", "w")
        arquivo.seek(0)
        for line in arquivo_de_configuracoes:
            arquivo.write(line)
        arquivo.close()

    def escrever_arquivo_de_resultados(self, diretorio_principal):
        numero_de_vertices_da_rede_original = self.administrador_de_dados_do_experimento.obter_total_de_vertices_da_rede_original()
        numero_de_arestas_da_rede_original = self.administrador_de_dados_do_experimento.obter_total_de_arestas_da_rede_original()
        numero_de_candidatos_a_link = self.administrador_de_dados_do_experimento.obter_numero_de_candidatos_a_link()
        numero_de_links_previstos = self.administrador_de_dados_do_experimento.obter_numero_de_links_previstos()
        numero_de_acertos = self.administrador_de_dados_do_experimento.obter_numero_de_acertos()
        numero_de_erros = self.administrador_de_dados_do_experimento.obter_numero_de_erros()

        texto  = "Rede Original \n\n"
        texto += "Vertices: " + str(numero_de_vertices_da_rede_original) + "\n"
        texto += "Arestas: " + str(numero_de_arestas_da_rede_original) + "\n"
        texto += "Candidatos a Link: " + str(numero_de_candidatos_a_link) + "\n"
        texto += "Previsoes Efetuadas: " + str(numero_de_links_previstos) + "\n"
        texto += "Acertos: " + str(numero_de_acertos) + "\n"
        texto += "Erros: " + str(numero_de_erros) + "\n"
            
        utils.escrever_em_txt(diretorio_principal, "resultados.txt", texto)

    def escrever_informacoes_das_redes(self):
        adm = self.administrador_de_dados_do_experimento
        self.escrever_informacoes_da_rede(adm.obter_rede_lida(), "Rede Original.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_treino(), "Rede de Treino.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_testes(), "Rede de Testes.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_treino_com_corte_core(), "Rede de Treino com Corte.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_testes_com_corte_core(), "Rede de Testes com Corte.txt")

    def escrever_informacoes_da_rede(self, rede, nome_do_arquivo):
        texto = "Rede: " + self.banco_de_dados_da_execucao.obter_nome_da_rede() + "\n"

        texto += "Vertices: \n"
        vertices = rede.obter_lista_de_vertices()
        for vertice in vertices:
            grau = rede.obter_grau_de_no(vertice)
            texto += str(vertice) + ", Grau: " + str(grau) + "\n"
        texto += "\n\n"

        texto += "Arestas: \n"
        arestas = rede.obter_lista_de_arestas()
        for aresta in arestas:
            texto += str(aresta) + "\n"
        texto += "\n\n"
        utils.escrever_em_txt(self.diretorio_de_resultados, nome_do_arquivo, texto)

    def escrever_arquivo_de_core(self, nome_do_arquivo):
        adm = self.administrador_de_dados_do_experimento

        texto = "Conjunto Core: \n"
        core  = adm.obter_conjunto_core()
        for vertice in core:
            texto += str(vertice) + "\n"
        texto += "\n\n"

        texto += "Arestas apos corte (testes):\n"
        arestas = adm.obter_arestas_da_rede_de_testes_com_corte_core()
        for aresta in arestas:
            texto += str(aresta) + "\n"
        texto += "\n\n"

        utils.escrever_em_txt(self.diretorio_de_resultados, nome_do_arquivo, texto)
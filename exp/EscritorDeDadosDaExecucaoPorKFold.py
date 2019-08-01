import os
from utilidades import utils as utils


class EscritorDeDadosDaExecucaoPorKFold():
    def __init__(self, banco_de_dados_da_execucao):
        self.banco_de_dados_da_execucao = banco_de_dados_da_execucao
        self.parametrizador = self.banco_de_dados_da_execucao.parametrizador
        self.texto_final_de_resultados = ''

    def escrever_resultados(self):
        self.diretorio_principal = self.criar_diretorio_de_resultados()
        self.escrever_arquivo_de_configuracoes(self.diretorio_principal, self.parametrizador.arquivo_de_parametros)
        for etapa in range(1, self.parametrizador.quantidade_de_etapas + 1):
            self.etapa_atual = etapa
            self.administrador_de_dados_do_experimento = self.banco_de_dados_da_execucao.bancos_de_dados_de_experimentos[etapa-1]
            self.escrever_resultados_por_fold(etapa)
        self.escrever_arquivo_de_resultados_global(self.diretorio_principal)
        print "Resultados Escritos"

    def escrever_resultados_por_fold(self, etapa):
        diretorio_por_fold = self.diretorio_principal + '/' + str(etapa).zfill(2)
        utils.criar_diretorio_se_nao_existir(diretorio_por_fold)
        self.escrever_arquivo_de_resultados(diretorio_por_fold)
        self.escrever_informacoes_das_redes(diretorio_por_fold)
        self.escrever_arquivo_de_core(diretorio_por_fold, "core.txt")

    def criar_diretorio_de_resultados(self):
        nome_da_rede = self.banco_de_dados_da_execucao.obter_nome_da_rede()
        nome_da_pasta = self.montar_nome_da_pasta()
        diretorio_principal = "../resultados/kfold/" + nome_da_rede + "/" + nome_da_pasta
        utils.criar_diretorio_se_nao_existir(diretorio_principal)
        return diretorio_principal

    def montar_nome_da_pasta(self):
        return str(self.parametrizador.quantidade_de_etapas) + ' Folds - Core ' + \
                                                 str(self.parametrizador.pcore_treino) + ' ' + \
                                                 str(self.parametrizador.pcore_testes) + ' - ' + \
                                                 self.parametrizador.estrategia_de_deteccao


    def escrever_arquivo_de_configuracoes(self, diretorio_de_resultados, arquivo_de_configuracoes):
        utils.criar_diretorio_se_nao_existir(diretorio_de_resultados)
        arquivo = open(diretorio_de_resultados + "/config.txt", "w")
        arquivo.seek(0)
        arquivo_de_configuracoes.seek(0)
        for line in arquivo_de_configuracoes:
            arquivo.write(line)
        arquivo.close()

    def escrever_arquivo_de_resultados(self, diretorio_principal):
        texto = self.montar_texto_de_resultados()
        utils.escrever_em_txt(diretorio_principal, "resultados.txt", texto)
        self.texto_final_de_resultados += texto + '\n\n\n'

    def montar_texto_de_resultados(self):
        numero_de_vertices_da_rede_original = self.administrador_de_dados_do_experimento.obter_total_de_vertices_da_rede_original()
        numero_de_arestas_da_rede_original = self.administrador_de_dados_do_experimento.obter_total_de_arestas_da_rede_original()
        numero_de_candidatos_a_link = self.administrador_de_dados_do_experimento.obter_numero_de_candidatos_a_link()
        numero_de_links_previstos = self.administrador_de_dados_do_experimento.obter_numero_de_links_previstos()
        numero_de_acertos = self.administrador_de_dados_do_experimento.obter_numero_de_acertos()
        numero_de_erros = self.administrador_de_dados_do_experimento.obter_numero_de_erros()

        texto = "FOLD " + str(self.etapa_atual) + '\n\n'
        texto += "Rede Original \n\n"
        texto += "Vertices: " + str(numero_de_vertices_da_rede_original) + "\n"
        texto += "Arestas: " + str(numero_de_arestas_da_rede_original) + "\n"
        texto += "Candidatos a Link: " + str(numero_de_candidatos_a_link) + "\n"
        texto += "Previsoes Efetuadas: " + str(numero_de_links_previstos) + "\n"
        texto += "Acertos: " + str(numero_de_acertos) + "\n"
        texto += "Erros: " + str(numero_de_erros) + "\n"

        #Temporario(?)
        import networkx as nx
        #G = utils.converter_multigrafo_nx_para_grafo_nx(self.administrador_de_dados_do_experimento.rede_de_treino.grafo_nx)
        G = nx.Graph(self.administrador_de_dados_do_experimento.rede_de_treino.grafo_nx)
        diff_treino = abs(G.number_of_edges() - self.administrador_de_dados_do_experimento.rede_de_treino.grafo_nx.number_of_edges())
        texto += "Numero de Multiarestas na rede treino: " + str(diff_treino) + '\n'
        #texto += "\nAki\n"
        #print(str(G.number_of_edges()) + ' ' + str(self.administrador_de_dados_do_experimento.rede_de_treino.grafo_nx.number_of_edges()))
        #print(G.edges())
        #print(self.administrador_de_dados_do_experimento.rede_de_treino.grafo_nx.edges())
        G = nx.Graph(self.administrador_de_dados_do_experimento.rede_de_testes.grafo_nx)
        diff_testes = abs(G.number_of_edges() - self.administrador_de_dados_do_experimento.rede_de_testes.grafo_nx.number_of_edges())
        texto += "Numero de Multiarestas na rede testes: " + str(diff_testes) + '\n'
        return texto

    def escrever_informacoes_das_redes(self, diretorio):
        adm = self.administrador_de_dados_do_experimento
        self.escrever_informacoes_da_rede(adm.obter_rede_lida(), diretorio, "Rede Original.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_treino(), diretorio, "Rede de Treino.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_testes(), diretorio, "Rede de Testes.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_treino_com_corte_core(), diretorio, "Rede de Treino com Corte.txt")
        self.escrever_informacoes_da_rede(adm.obter_rede_de_testes_com_corte_core(), diretorio, "Rede de Testes com Corte.txt")

    def escrever_informacoes_da_rede(self, rede, diretorio, nome_do_arquivo):
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
        utils.escrever_em_txt(diretorio, nome_do_arquivo, texto)

    def escrever_arquivo_de_core(self, diretorio, nome_do_arquivo):
        adm = self.administrador_de_dados_do_experimento

        texto = "Conjunto Core: \n"
        core = adm.obter_conjunto_core()
        for vertice in core:
            texto += str(vertice) + "\n"
        texto += "\n\n"

        texto += "Arestas apos corte (testes):\n"
        arestas = adm.obter_arestas_da_rede_de_testes_com_corte_core()
        for aresta in arestas:
            texto += str(aresta) + "\n"
        texto += "\n\n"

        utils.escrever_em_txt(diretorio, nome_do_arquivo, texto)

    def escrever_arquivo_de_resultados_global(self, diretorio_de_resultados):
        utils.criar_diretorio_se_nao_existir(diretorio_de_resultados)
        arquivo = open(diretorio_de_resultados + "/resultados_globais.txt", "w")
        arquivo.seek(0)
        arquivo.write(self.texto_final_de_resultados)
        arquivo.close()

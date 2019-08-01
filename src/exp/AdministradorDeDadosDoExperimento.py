class AdministradorDeDadosDoExperimento():
    def __init__(self):
        pass

    def atribuir_data_e_hora_de_inicio_do_experimento(self, data_e_hora):
        self.data_e_hora_de_inicio = data_e_hora

    def atribuir_data_e_hora_de_fim_do_experimento(self, data_e_hora):
        self.data_e_hora_de_fim = data_e_hora

    def atribuir_rede_lida(self, rede_lida):
        self.rede_lida = rede_lida

    def atribuir_redes_de_treino_e_teste(self, rede_de_treino, rede_de_testes):
        self.rede_de_treino, self.rede_de_testes = rede_de_treino, rede_de_testes

    def atribuir_conjuntos_core(self, conjunto_core_treino, conjunto_core_testes, conjunto_core):
        self.conjunto_core_treino = conjunto_core_treino
        self.conjunto_core_testes = conjunto_core_testes
        self.conjunto_core        = conjunto_core

    def atribuir_redes_pcore(self, rede_de_treino_pcore, rede_de_testes_pcore):
        self.rede_de_treino_com_corte_core = rede_de_treino_pcore
        self.rede_de_testes_com_corte_core = rede_de_testes_pcore

    def atribuir_particionamento(self, particionamento):
        self.particionamento = particionamento

    def atribuir_numero_de_links_previstos(self, n):
        self.numero_de_links_previstos = n

    def obter_total_de_vertices_da_rede_original(self):
        return self.rede_lida.obter_numero_de_vertices()

    def obter_total_de_arestas_da_rede_original(self):
        return self.rede_lida.obter_numero_de_arestas()

    def obter_lista_de_arestas_da_rede(self):
        return self.rede_lida.obter_lista_de_arestas()

    def atribuir_links_previstos(self, links_previstos):
        self.links_previstos = links_previstos

    def obter_links_previstos(self):
        return self.links_previstos
    
    def obter_numero_de_links_previstos(self):
        return len(self.obter_links_previstos())

    def atribuir_candidatos_a_link(self, candidatos_a_link):
        self.candidatos_a_link = candidatos_a_link

    def obter_numero_de_candidatos_a_link(self):
        return len(self.candidatos_a_link)

    def obter_numero_de_acertos(self):
        return self.numero_de_acertos

    def obter_numero_de_erros(self):
        return self.numero_de_erros

    def atribuir_links_previstos_corretamente(self, links_previstos_corretamente):
        self.links_previstos_corretamente = links_previstos_corretamente

    def atribuir_links_realizados(self, links_realizados):
        self.links_realizados = links_realizados

    def atribuir_numero_de_acertos(self, numero_de_acertos):
        self.numero_de_acertos = numero_de_acertos

    def atribuir_numero_de_erros(self, numero_de_erros):
        self.numero_de_erros = numero_de_erros

    def obter_vertices_da_rede_original(self):
        return self.rede_lida.obter_lista_de_vertices()

    def obter_arestas_da_rede_original(self):
        return self.rede_lida.obter_lista_de_arestas()

    def obter_vertices_da_rede_de_treino(self):
        return self.rede_de_treino.obter_lista_de_vertices()

    def obter_arestas_da_rede_de_treino(self):
        return self.rede_de_treino.obter_lista_de_arestas()

    def obter_vertices_da_rede_de_testes(self):
        return self.rede_de_testes.obter_lista_de_vertices()

    def obter_arestas_da_rede_de_testes(self):
        return self.rede_de_testes.obter_lista_de_arestas()

    def obter_vertices_da_rede_de_treino_com_corte_core(self):
        return self.rede_de_treino_com_corte_core.obter_lista_de_vertices()

    def obter_arestas_da_rede_de_treino_com_corte_core(self):
        return self.rede_de_treino_com_corte_core.obter_lista_de_arestas()

    def obter_vertices_da_rede_de_testes_com_corte_core(self):
        return self.rede_de_testes_com_corte_core.obter_lista_de_vertices()

    def obter_arestas_da_rede_de_testes_com_corte_core(self):
        return self.rede_de_testes_com_corte_core.obter_lista_de_arestas()

    def obter_conjunto_core(self):
        return self.conjunto_core

    def obter_conjunto_core_treino(self):
        return self.conjunto_core_treino

    def obter_conjunto_core_testes(self):
        return self.conjunto_core_testes

    def obter_rede_lida(self):
        return self.rede_lida

    def obter_rede_de_treino(self):
        return self.rede_de_treino

    def obter_rede_de_testes(self):
        return self.rede_de_testes

    def obter_rede_de_treino_com_corte_core(self):
        return self.rede_de_treino_com_corte_core

    def obter_rede_de_testes_com_corte_core(self):
        return self.rede_de_testes_com_corte_core


# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
import utilidades.utils as utils

class AdministradorDaEtapaDeCorteCore(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        rede_de_treino = self.experimento.rede_de_treino
        rede_de_testes = self.experimento.rede_de_testes

        print("Removendo vertices que nao pertencem ao conjunto core...")
        self._aplicar_corte_pcore(rede_de_treino, rede_de_testes, self.experimento.parametrizador, self.experimento.rede)

        print("Numero de vertices no core (treino):", len(self.rede_de_treino_pcore.obter_lista_de_nos()))
        print("Numero de vertices no core (testes):", len(self.rede_de_testes_pcore.obter_lista_de_nos()))

        print("Corte core aplicado. Arestas em rede de testes: ")
        n = self.rede_de_testes_pcore.obter_lista_de_arestas()
        print n
        print("Numero de Arestas em Rede de Treino e Rede de Testes:")
        print(self.rede_de_treino_pcore.obter_numero_de_arestas(), self.rede_de_testes_pcore.obter_numero_de_arestas())

        self._atribuir_parametros_ao_administrador_de_dados()

        return self.rede_de_treino_pcore, self.rede_de_testes_pcore

    def _aplicar_corte_pcore(self, rede_de_treino, rede_de_testes, parametrizador, rede_original):
        self.conjunto_core_treino = self.obter_lista_de_vertices_por_grau_minimo(rede_de_treino, parametrizador.pcore_treino)
        self.conjunto_core_testes = self.obter_lista_de_vertices_por_grau_minimo(rede_de_testes, parametrizador.pcore_testes)
        self.conjunto_core = utils.intercessao_de_listas(self.conjunto_core_treino, self.conjunto_core_testes)

        self.vertices_fora_do_core = self._obter_vertices_que_nao_pertencem_ao_conjunto(rede_original, self.conjunto_core)

        self.rede_de_treino_pcore = rede_de_treino.obter_rede_equivalente_removendo_lista_de_vertices(self.vertices_fora_do_core)
        self.rede_de_testes_pcore = rede_de_testes.obter_rede_equivalente_removendo_lista_de_vertices(self.vertices_fora_do_core)

    def obter_lista_de_vertices_por_grau_minimo(self, rede, grau_minimo):
        lista_de_nos = []
        graus_dos_nos = rede.obter_graus().items()
        for no, grau in graus_dos_nos:
            if grau >= grau_minimo:
                lista_de_nos.append(no)
        return lista_de_nos

    def _obter_vertices_que_nao_pertencem_ao_conjunto(self, rede, vertices_a_serem_removidos):
        lista_de_vertices = list(rede.obter_lista_de_vertices())
        for vertice in vertices_a_serem_removidos:
            lista_de_vertices.remove(vertice)
        return lista_de_vertices

    def _atribuir_parametros_ao_administrador_de_dados(self):
        administrador = self.experimento.administrador_de_dados_do_experimento
        administrador.atribuir_conjuntos_core(self.conjunto_core_treino,
                                              self.conjunto_core_testes,
                                              self.conjunto_core)
        administrador.atribuir_redes_pcore(self.rede_de_treino_pcore,
                                           self.rede_de_testes_pcore)
from nucleo.Rede import Rede
import networkx as nx
import utilidades.utils as utils
from nucleo.LeitorGraphMl import LeitorGraphML

class ParticionadorDeRede():

    def __init__(self):
        pass

    def separar_rede_por_kfold(self, rede, etapa, quantidade_de_etapas):
        rede_de_treino = rede.copia()

        lista_de_links = rede.obter_lista_de_links()
        total = len(lista_de_links)
        tamanho_do_conjunto = total / quantidade_de_etapas
        i = etapa
        links_de_teste = lista_de_links[(i-1) * tamanho_do_conjunto : (i) * tamanho_do_conjunto]
        rede_de_treino = rede_de_treino.obter_rede_equivalente_removendo_lista_de_links(links_de_teste)
        G = nx.Graph()
        G.add_edges_from(links_de_teste)
        nos_em_G = list(G.nodes())

        nos = list(rede.obter_lista_de_vertices())
        for no in nos:
            if no not in nos_em_G:
                G.add_node(no)

        rede_de_testes = Rede(G)
        return (rede_de_treino, rede_de_testes)

    def separar_rede_por_periodo(self, rede, periodo_de_treino, periodo_de_testes, palavra_chave_que_identifica_ano, caminho_da_rede = ''):
        arquivo_de_treino = caminho_da_rede + " - TREINO" + str(periodo_de_treino) + '.txt'
        arquivo_de_testes = caminho_da_rede + " - TESTES" + str(periodo_de_testes) + '.txt'
        if utils.arquivo_existe(arquivo_de_treino):
            rede_de_treino = LeitorGraphML().ler_graphml(arquivo_de_treino)
        else:
            print("Identificando rede de treino...")
            rede_de_treino = self._obter_rede_em_periodo(rede, periodo_de_treino, palavra_chave_que_identifica_ano)
            LeitorGraphML().escrever_graphml(arquivo_de_treino, rede_de_treino.grafo_nx)
        if utils.arquivo_existe(arquivo_de_testes):
            rede_de_testes = LeitorGraphML().ler_graphml(arquivo_de_testes)
        else:
            print("Identificando rede de testes...")
            rede_de_testes = self._obter_rede_em_periodo(rede, periodo_de_testes, palavra_chave_que_identifica_ano)
            LeitorGraphML().escrever_graphml(arquivo_de_testes, rede_de_testes.grafo_nx)
        return (rede_de_treino, rede_de_testes)

    def _obter_rede_em_periodo(self, rede, periodo, palavra_ano):
        grafonx = nx.MultiGraph()
        grafonx.add_nodes_from(rede.obter_lista_de_vertices())
        progresso = 0
        links = rede.obter_lista_de_links_com_atributos()
        novos_links = []
        total_de_links = len(links)
        for link in links:
            if int(link[2][palavra_ano]) >= periodo[0] and int(link[2][palavra_ano]) <= periodo[1]:
                novos_links.append(link)
            progresso += 1
            utils.apresentar_mensagem_de_progresso(progresso, total_de_links)
        grafonx.add_edges_from(novos_links)
        nova_rede = Rede(grafonx, "Rede de Treino " + str(periodo))
        return nova_rede

    def aplicar_corte_pcore(self, rede_de_treino, rede_de_testes, pcore_treino, pcore_testes):
        vertices_fora_do_core_treino = self._obter_lista_de_vertices_de_grau_inferior_ao_minimo(rede_de_treino, pcore_treino)
        vertices_fora_do_core_testes = self._obter_lista_de_vertices_de_grau_inferior_ao_minimo(rede_de_testes, pcore_testes)
        vertices_a_serem_removidos = utils.mesclar_listas(vertices_fora_do_core_treino, vertices_fora_do_core_testes)
        rede_de_treino_pcore = rede_de_treino.obter_rede_equivalente_removendo_lista_de_vertices(vertices_a_serem_removidos)
        rede_de_testes_pcore = rede_de_testes.obter_rede_equivalente_removendo_lista_de_vertices(vertices_a_serem_removidos)
        return rede_de_treino_pcore, rede_de_testes_pcore

    def _obter_lista_de_vertices_de_grau_inferior_ao_minimo(self, rede, grau_minimo):
        lista_de_nos = []
        graus_dos_nos = rede.obter_graus().items()
        for no, grau in graus_dos_nos:
            if grau < grau_minimo:
                lista_de_nos.append(no)
        return lista_de_nos
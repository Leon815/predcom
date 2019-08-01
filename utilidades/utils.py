import os
from math import pow
from math import factorial
from datetime import datetime
import networkx as nx

def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def arquivo_existe(caminho):
    return os.path.isfile(caminho)

def formatar_aresta_para_exibicao(aresta):
    return (aresta[0] + 1, aresta[1] + 1)

def formatar_lista_de_arestas_para_exibicao(lista_de_arestas):
    lista_formatada = []
    for aresta in lista_de_arestas:
        lista_formatada.append(formatar_aresta_para_exibicao(aresta))
    return lista_formatada

def zero(valor, precisao = 12):
    if abs(valor) < pow(10, -precisao):
        return True
    else:
        return False

def quantidade_de_combinacoes(n, r):
    return (factorial(n) / factorial(n - r)) / factorial(r)

def quantidade_de_permutacoes(n, r):
    return (factorial(n) / factorial(n - r))

def arredondar_entradas_de_matriz(matriz, casas_decimais):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = round(matriz[i][j], casas_decimais)
    return matriz

def mesclar_listas(lista_a, lista_b):
    elementos_apenas_na_lista_b = set(lista_b) - set(lista_a)
    return lista_a + list(elementos_apenas_na_lista_b)

def intercessao_de_listas(lista_a, lista_b):
    intercessao = []
    for elemento in lista_a:
        if elemento in lista_b:
            intercessao.append(elemento)
    return intercessao

def apresentar_mensagem_de_progresso(progresso, total, salto_percentual=5):
    salto = round(total / round(100/salto_percentual, 4), 0)
    if salto == 0:
        return
    if progresso % salto == 0:
        percentual = round((100.0 / total) * progresso, 0)
        print("Progresso: " + str(percentual) + " (" + str(progresso) + " de " + str(total) + ").")

def extrair_nome_de_arquivo_de_diretorio_completo(diretorio_completo):
    nome, extensao = os.path.splitext(diretorio_completo)
    return os.path.basename(nome)

def extrair_diretorio(diretorio_completo):
    return os.path.dirname(diretorio_completo)

def momento():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def escrever_em_txt(diretorio, nome_do_arquivo, texto):
    criar_diretorio_se_nao_existir(diretorio)
    arquivo = open(diretorio + "/" + nome_do_arquivo, "w")
    arquivo.write(texto)

def converter_multigrafo_nx_para_grafo_nx(multigrafo):
    G = nx.Graph()
    vertices = multigrafo.nodes()
    arestas = multigrafo.edges()

    for vertice in vertices:
        G.add_node(vertice)

    for aresta in arestas:
        arestas_de_g = list(G.edges())
        if aresta not in arestas_de_g:
            G.add_edge(aresta[0], aresta[1])
    return G
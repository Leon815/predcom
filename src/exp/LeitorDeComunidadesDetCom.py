from lxml import objectify

class LeitorDeComunidadesDetCom():
    def ler_comunidades_de_rede(self, caminho_do_arquivo_dynetwork_de_entrada_do_detcom, caminho_do_arquivo_de_saida_do_detcom):
        arquivo_de_entrada = open(caminho_do_arquivo_dynetwork_de_entrada_do_detcom)
        arquivo_de_saida = open(caminho_do_arquivo_de_saida_do_detcom)
        correspondencia = self.construir_correspondencia_de_inteiro_para_labels(arquivo_de_entrada)
        particionamento = self.obter_particionamento(correspondencia, arquivo_de_saida)
        return particionamento

    def construir_correspondencia_de_inteiro_para_labels_detcom(self, rede, arquivo_original_da_rede):
        correspondencia = {}
        i = 0
        xml = arquivo_original_da_rede.read()
        root = objectify.fromstring(xml)
        for graph in root.getchildren():
            for element in graph.getchildren():
                node = element.get("id")
                if not node:
                    source = element.get("source")
                    target = element.get("target")
                    if source not in correspondencia.values():
                        correspondencia[i] = source
                        i += 1
                    if target not in correspondencia.values():
                        correspondencia[i] = target
                        i += 1
        print(correspondencia)
        return correspondencia

    def construir_correspondencia_de_inteiro_para_labels(self, arquivo_original_da_rede):
        correspondencia = {}
        i = 0
        xml = arquivo_original_da_rede.read()

        root = objectify.fromstring(xml)
        for graph in root.getchildren():
            if graph.tag == 'MetaNetwork':
                for elemento_do_grafo in graph.getchildren():
                    if elemento_do_grafo.tag == 'nodes':
                        for informacoes in elemento_do_grafo.getchildren():
                            if informacoes.tag == 'nodeclass':
                                for node in informacoes.getchildren():#Nos
                                    id = int(node.attrib["id"])
                                    id_antigo = node.properties.property.attrib["value"]
                                    correspondencia[id] = id_antigo
        print(correspondencia)
        return correspondencia


    def obter_particionamento(self, correspondencia, arquivo_detcom):
        lista_de_comunidades = []

        #Inicializa o dicionario de particionamento
        particionamento = {}
        for _, valor in correspondencia.items():
            particionamento[valor] = []

        for line in arquivo_detcom:
            if line == 'GN\n': break
            if line[0] == '{':
                comunidades_do_subgrafo = eval(line)
                for id, comunidade in comunidades_do_subgrafo.items():
                    lista_de_comunidades.append(comunidade)

        id_comunidade = 0
        for comunidade in lista_de_comunidades:
            for id_vertice in comunidade:
                vertice = correspondencia[id_vertice]
                particionamento[vertice].append(id_comunidade)
            id_comunidade += 1

        print(particionamento)
        return particionamento

    def obter_nome(self):
        return "ComunidadesDetcom"

'''arquivo_detcom = open("ArquivosDetCom\\Results_arxivNetwork.txt")

from Rede import Rede
import networkx as nx

g = nx.Graph()
g.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7"])
rede = Rede(g)

leitor = LeitorDeComunidadesDetCom()
particionamento = leitor.executar_estrategia(rede)'''
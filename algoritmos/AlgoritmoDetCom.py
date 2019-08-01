import utilidades.girvan_newman_kjahan as girvan_newman_kjahan
from DeteccaoDeComunidadesStrategy import EstrategiaDeDeteccaoDeComunidades
from nucleo.LeitorGraphMl import LeitorGraphML
from detcom import arxivToDetCom, detcom
from exp.LeitorDeComunidadesDetCom import LeitorDeComunidadesDetCom

class AlgoritmoDetCom(EstrategiaDeDeteccaoDeComunidades):
    def _executar(self, rede):
        caminho_graphml   = "detcomNV/dataset/rede_detcom_graphml.xml"
        caminho_dynetwork = "detcomNV/dataset/rede_detcom_dynetwork.xml"
        caminho_de_saida_detcom = "detcomNV/output/Results_arxivNetwork.txt"
        LeitorGraphML().escrever_graphml(caminho_graphml, rede.grafo_nx)
        arxivToDetCom.converter(caminho_graphml, caminho_dynetwork)
        detcom.executar(caminho_dynetwork)
        particionamento = LeitorDeComunidadesDetCom().ler_comunidades_de_rede(caminho_dynetwork, caminho_de_saida_detcom)
        return particionamento

    def obter_nome(self):
        return "DetCom"

#from Rede import Rede
#alg = AlgoritmoDetCom()
#particionamento = alg.executar_estrategia(LeitorGraphML().ler_graphml("detcomNV/dataset/rede_de_entrada_graphml.txt"))
#print particionamento
# -*- coding: utf-8 -*-
__author__ = 'Márcio Vinícius Dias'


import step1, step3, step4, step5, step6


class Main():

    attribSelecteds = {}
    metaPath = []


    def __init__(self):
        pass

    def run(self, caminho_da_rede_de_entrada = ''):
        # ***********************************************************
        # STEP ONE INIT

        #xmlFileSchema = 'dataset/esquema_rede_enronNetwork.xml'
        # verticesAndAttribFromSchema = step1.Etp1().getAllVerticesAndAttribFromSchema( xmlFileSchema)
        # print verticesAndAttribFromSchema

        #self.metaPath.append('pessoa')
        #self.metaPath.append('pessoa-1')
        #self.metaPath.append('ocorrencia')

        #self.attribSelecteds['pessoa'] = ['name']
        #self.attribSelecteds['ocorrencia'] = ['latitude', 'longitude', 'dataHora']

        #AKI
        #xmlFileNetworkGi = 'detcomNV/' + 'dataset/rede_camila.xml'
        if caminho_da_rede_de_entrada == '':
            xmlFileNetworkGi = 'dataset/rede_detcom_dynetwork.xml'
        else:
            xmlFileNetworkGi = caminho_da_rede_de_entrada
        #nameOfNetwork = 'abordagemNetwork'
        #targetVertice = 'pessoa'
        #attrbToLabel = 'name'
        self.metaPath.append('author')
        self.metaPath.append('author-1')
        self.attribSelecteds['author'] = ['bagOfWords', 'year']
        self.attribSelecteds['author-1'] = ['bagOfWords', 'year']
        #xmlFileNetworkGi = 'dataset/detcom22_06.xml'
        nameOfNetwork = 'arxivNetwork'
        targetVertice = 'author'
        attrbToLabel = 'name'
        categorical = True
        isHomogeneousNetwork = True

        # print "Step1 done!"

        # STEP ONE END
        # ***********************************************************

        # ***********************************************************
        # STEP THREE INIT
        fileToSaveRecords = 'detcomNV/output/records.txt'
        step3.Etp3().run(xmlFileNetworkGi, self.metaPath, self.attribSelecteds, fileToSaveRecords, isHomogeneousNetwork)

        # STEP THREE END
        # ***********************************************************

        # ***********************************************************
        # STEP FOUR INIT
        fileWithTreatedRecords = 'detcomNV/output/recordsForClustering.txt'
        step4.Etp4().run(fileWithTreatedRecords, fileToSaveRecords, categorical, isHomogeneousNetwork)

        # STEP FOUR END
        # ***********************************************************

        # ***********************************************************
        # STEP FIVE INIT
        fileWithClusters = 'detcomNV/output/clusters.txt'
        fileInducedGraph = 'detcomNV/output/inducedGraph4.txt'
        step5.Etp5().run(fileWithClusters, fileToSaveRecords, fileInducedGraph, targetVertice, isHomogeneousNetwork)

        # STEP FIVE END
        # ***********************************************************

        # ***********************************************************
        # STEP SIX INIT
        step6.Etp6().run(fileInducedGraph, targetVertice, nameOfNetwork, attrbToLabel, xmlFileNetworkGi)

        # STEP SIX END
        # ***********************************************************

        # STEP SIX INIT
        #step6.Etp6().run(fileInducedGraph, targetVertice, nameOfNetwork, attrbToLabel, xmlFileNetworkGi)

        #fit2.Etp8().run(fileWithClusters, fileToSaveRecords, fileInducedGraph, targetVertice, isHomogeneousNetwork)

        # STEP SIX END
        # ***********************************************************


        # ***********************************************************
        # STEP SEVEN INIT
        #step7.Etp7().run(targetVertice, nameOfNetwork, attrbToLabel, xmlFileNetworkGi)

        # STEP SEVEN END
        # ***********************************************************


# if __name__ == "__main__":
#     print(__doc__)
#     Main().run()

def executar(caminho_rede_dynetwork):
    Main().run(caminho_rede_dynetwork)
    print "detcomNV executado - Results_arxivNetwork.txt escrito"
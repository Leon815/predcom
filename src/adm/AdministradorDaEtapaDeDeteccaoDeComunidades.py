# -*- coding: utf-8 -*-
import abc
from AdministradorDeEtapasAbstrato import AdministradorDeEtapasAbstrato
from algoritmos.AlgoritmoDeLouvain import AlgoritmoDeLouvain
from algoritmos.AlgoritmoDetCom import AlgoritmoDetCom
from algoritmos.AlgoritmoGirvanKjahan import AlgoritmoGirvanKjahan
from algoritmos.AlgoritmoGirvanNetworkX import AlgoritmoGirvan
from exp.DetectorDeComunidades import DetectorDeComunidades

class AdministradorDaEtapaDeDeteccaoDeComunidades(AdministradorDeEtapasAbstrato):
    def executar_etapa(self):
        self.estrategia_de_deteccao = self._identificar_detector_de_comunidades(self.experimento.parametrizador)
        detector_de_comunidades = DetectorDeComunidades(self.estrategia_de_deteccao)
        print('Detectando Comunidades...')
        self.particionamento = detector_de_comunidades.detectar_comunidades(self.experimento.rede_de_treino_core)
        print(self.particionamento)
        self.experimento.administrador_de_dados_do_experimento.atribuir_particionamento(self.particionamento)
        return self.particionamento

    def _identificar_detector_de_comunidades(self, parametrizador):
        if parametrizador.estrategia_de_deteccao == "louvain":
            return AlgoritmoDeLouvain()
        elif parametrizador.estrategia_de_deteccao == "detcomNV":
            return AlgoritmoDetCom()
        elif parametrizador.estrategia_de_deteccao == "girvan":
            return AlgoritmoGirvanKjahan
        elif parametrizador.estrategia_de_deteccao == "girvannx":
            return AlgoritmoGirvan()
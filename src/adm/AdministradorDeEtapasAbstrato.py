import abc

class AdministradorDeEtapasAbstrato():
    __metaclass__ = abc.ABCMeta

    def __init__(self, experimento):
        self.experimento = experimento

    @abc.abstractmethod
    def executar_etapa(self):
        pass

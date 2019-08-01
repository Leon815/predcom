from abc import ABCMeta, abstractmethod

class EstrategiaDeDeteccaoDeComunidades:
    __metaclass__ = ABCMeta

    def executar_estrategia(self, rede):
        return self._executar(rede)

    @abstractmethod
    def _executar(self, rede):
        raise NotImplementedError()

    @abstractmethod
    def obter_nome(self):
        raise NotImplementedError()
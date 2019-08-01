class DetectorDeComunidades:
    def __init__(self, estrategia_de_deteccao_de_comunidades):
        self.particionamento = -1
        self.estrategia_de_deteccao_de_comunidades = estrategia_de_deteccao_de_comunidades

    def detectar_comunidades(self, rede):
        print("Executando " + self.estrategia_de_deteccao_de_comunidades.obter_nome())
        self.particionamento = self.estrategia_de_deteccao_de_comunidades.executar_estrategia(rede)
        #self.escrever_particoes_em_txt()
        return self.particionamento

    def escrever_particoes_em_txt(self):
        nome_da_estrategia = self.estrategia_de_deteccao_de_comunidades.obter_nome()
        texto = "Algoritmo: " + nome_da_estrategia
        arquivo = open("resultados/particoes_geradas_" + nome_da_estrategia + ".txt", "w")
        texto += "\n Particionamento: \n\n" + self.particionamento.__str__()
        arquivo.write(texto)
        arquivo.close()

    def obter_comunidades_como_lista(self, rede):
        particionamento = self.detectar_comunidades(rede)
        lista_de_comunidades = []
        for id_comunidade in set(particionamento.values()):
            lista_de_nos = [no for no in particionamento.keys() if particionamento[no] == id_comunidade]
            lista_de_comunidades.append(lista_de_nos)
        return lista_de_comunidades
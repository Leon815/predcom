from CalculadorDeMetricas import CalculadorDeMetricas

class RankingDePontos:
    pontuacoes = []

    def __init__(self, rede, particionamento = []):
        self.rede = rede
        self.particionamento = particionamento
        self.calculador_de_metricas = CalculadorDeMetricas(self.rede)

    def calcular_pontuacao(self, link, particionamento):
        pontuacao = 0
        #pontuacao += self.calculador_de_metricas.calcular_metrica_vizinhos_em_comum(link)
        # pontuacao += self.calculador_de_metricas.calcular_metrica_similaridade_de_jaccard(link)
        # pontuacao += self.calculador_de_metricas.calcular_similaridade_de_sorensen(link)
        # pontuacao += self.calculador_de_metricas.calcular_alocacao_de_recursos(link)
        #pontuacao += self.calculador_de_metricas.calcular_Leicht_Holme_Newman(link)
        pontuacao += self.calculador_de_metricas.calcular_metrica_vizinhos_em_comum_1(link, particionamento)
        #pontuacao += self.calculador_de_metricas.calcular_metrica_vizinhos_em_comum_2(link, particionamento)

        #pontuacao += self.calculador_de_metricas.calcular_metrica_vizinhos_em_comum_3(link, particionamento)
        #pontuacao += self.calculador_de_metricas.calcular_metrica_vizinhos_em_comum_1(link, particionamento)
        return pontuacao

    def calcular_pontuacao_dos_links(self, lista_de_links):
        pontuacoes = []
        progresso = 0
        for link in lista_de_links:
            self.exibir_mensagem_de_progresso(progresso, len(lista_de_links))
            pontuacao = self.calcular_pontuacao(link, self.particionamento)
            pontuacoes.append((link, pontuacao))
            progresso += 1
        self.pontuacoes = sorted(pontuacoes, key=lambda x: x[1], reverse=True) #Ordenacao da lista
        self.exibir_pontuacoes()

    def exibir_pontuacoes(self):
        for pontuacao in self.pontuacoes:
            if pontuacao[1] != 0:
                print("CandidatoALink:", (pontuacao[0]["no_a"], pontuacao[0]["no_b"]), "Pontuacao:", pontuacao[1])

    def escrever_pontuacoes(self, nome_do_arquivo):
        arquivo = open(nome_do_arquivo, 'w')
        arquivo.write("Iniciando Escrita" + "\n")
        texto = ''
        for pontuacao in self.pontuacoes:
            texto += "Candidato a Link: " + str(pontuacao[0]["no_a"]) + " , " + str(pontuacao[0]["no_b"]) + "Pontuacao:" + str(pontuacao[1]) + "\n"
        arquivo.write(texto)
        arquivo.close()

    def obter_pontuacoes(self):
        return self.pontuacoes

    def obter_n_links_de_pontuacoes_mais_altas(self, n):
        n_links = []
        if n > len(self.pontuacoes):
            print("Aviso: O n de corte (" + str(n) + ") maior que o numero de possibilidades (" + str(len(self.pontuacoes)) + ")")
            print("O n utilizado sera " + str(str(len(self.pontuacoes))))
            n = len(self.pontuacoes)

        for id_link in range(0, n):
            aresta = (self.pontuacoes[id_link][0]["no_a"], self.pontuacoes[id_link][0]["no_b"])
            n_links.append(aresta)
        return n_links

    def exibir_mensagem_de_progresso(self, progresso, total):
        if progresso % 100000 == 0:
           mensagem = "Calculando pontuacao de link " + str(progresso) + " de " + str(total)
           print(mensagem)

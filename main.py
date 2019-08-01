# -*- coding: utf-8 -*-
from Execucao import Execucao
import os
import src.exp as exp

if __name__ == "__main__":
    diretorio_de_configuracoes = os.path.abspath("../config.txt")
    arquivo_de_parametros = open(diretorio_de_configuracoes)
    execucao = Execucao(arquivo_de_parametros)
    execucao.executar()

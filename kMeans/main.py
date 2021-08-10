# -*- coding: utf-8 -*-
import numpy as np
from KMeans import KMeans

import os

def getDataset(nomearquivo):
    #O nome do diretório+arquivo.
    nomearquivo = os.path.abspath("./datasets/"+nomearquivo)
    #Verifica-se o arquivo existe.
    if not os.path.isfile(nomearquivo):
        raise Exception("Arquivo não encontrado")
    #Se existe, abre em modo de leitura.
    file = open(nomearquivo, "r", encoding="utf-8")
    #Tratamento para tirar dados indesejados
    labels = file.readline().replace("\t",",").replace(" ",",").replace("\n","").split(",")
    #Armazenará os ids
    ids = []
    #Armazenará os valores.
    dataset = []
    for line in file:
        line = line.replace("\t",",").replace(" ",",").replace("\n","")
        line = line.split(",")
        #if len(line) != 3:
        #    print(line)
        #    raise Exception("Erro no tratamento")
    
        dataset.append(np.array([float(value) for idx, value in enumerate(line) if idx > 0]))
        ids.append(line[0])
    file.close()
    return {"labels": labels, "ids":ids, "dataset":np.array(dataset)}

try:

#    nomearquivo = "c2ds1-2sp.txt" #spirals - 2 clusters
#    nomearquivo = "c2ds3-2g.txt" #globulars - 2 cluster
#    nomearquivo = "monkey.txt" #monkey 8 clusters

#    kClusters = 12
#    maxIteracoes = 5000

    print("Digite o nome do arquivo COM extensão")
    nomearquivo = input()
    print("Digite a quantidade de clusters desejado")
    kClusters = int(input())
    print("Digite o número de iterações")
    maxIteracoes = int(input())

    dit = getDataset(nomearquivo)
    kMeans = KMeans(dit["dataset"], dit["ids"], kClusters=kClusters, maxIteracoes=maxIteracoes, temSeed=True)
    
    
    iteracoes = kMeans.exec()
    kMeans.saidaArquivo("k"+str(kClusters)+".clu")
    kMeans.imagem()
    
except Exception as exc:
    print(exc)


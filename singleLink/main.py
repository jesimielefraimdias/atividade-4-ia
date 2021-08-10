# -*- coding: utf-8 -*-
import numpy as np
from SingleLink import SingleLink

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
        array = np.array([float(value) for idx, value in enumerate(line) if idx > 0])
        dataset.append(array)
        ids.append(line[0])
    file.close()
    return {"labels": labels, "ids":ids, "dataset":np.array(dataset)}

try:
    #nomearquivo = "c2ds1-2sp.txt" #spirals - 2 clusters
    #nomearquivo = "c2ds3-2g.txt" #globulars - 2 cluster
    #nomearquivo = "monkey.txt" #monkey 8 clusters


    #kMin=5
    #kMax=12
    print("Digite o nome do arquivo COM extensão")
    nomearquivo = input()
    print("Digite a quantidade minima de cluster")
    kMin = int(input())
    print("Digite a quantidade maxima de cluster")
    kMax = int(input())

    dit = getDataset(nomearquivo)
    singleLink = SingleLink(dit["dataset"], dit["ids"], kMin, kMax)
    
    singleLink.exec()

    
except Exception as exc:
    print(exc)


#Inicializamos o objeto KMeans com


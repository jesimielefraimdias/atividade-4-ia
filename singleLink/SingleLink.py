import matplotlib.pyplot as plt
import numpy as np
import os

from numpy.core.fromnumeric import argmin

class SingleLink:
    def __init__(self, dataset, ids, kMin, kMax):
        # A identificação dos elementos (ou pontos)
        self.ids = ids
        # Inicializa o número de cluster desejado.
        self.kMin = kMin
        self.kMax = kMax
        self.dataset = []
        self.pontos = dataset
        # Inicializa o dataset
        for indiceI, pontoI in enumerate(dataset):
            self.dataset.append({
                "cluster": [indiceI],
                "distancias":np.array([
                    self._distanciaEuclidiana(pontoI, pontoJ) for indiceJ, pontoJ in 
                    enumerate(dataset) if indiceJ < indiceI
                ])
            })
   
    def exec(self):
        
        n = len(self.dataset)
        
        while n >= self.kMin:
            if n <= self.kMax:
                self.imagem()
                self.saidaArquivo("k"+str(n)+".clu")

            i, j = self.closest()

            #Atualizando a linha j, pois ela é o que se manterá.
            for k in range(j):
                if self.dataset[j]["distancias"][k] > self.dataset[i]["distancias"][k]:
                    self.dataset[j]["distancias"][k] = self.dataset[i]["distancias"][k]

            #Atualizando os valores da coluna j para todas as linhas > i
            for indice, _ in enumerate(self.dataset[j+1:], start=j+1):
                if  (indice < i) and (self.dataset[indice]["distancias"][j] > self.dataset[i]["distancias"][indice]):
                    self.dataset[indice]["distancias"][j] = self.dataset[i]["distancias"][indice]

                elif indice > i and (self.dataset[indice]["distancias"][j] > self.dataset[indice]["distancias"][i]):
                    self.dataset[indice]["distancias"][j] = self.dataset[indice]["distancias"][i]
            
                if indice > i:
                    self.dataset[indice]["distancias"] = np.delete(self.dataset[indice]["distancias"], i, 0)
                
            for indice in self.dataset[i]["cluster"]:
                self.dataset[j]["cluster"].append(indice)
            self.dataset.pop(i)
            n-=1

    def closest(self):
        pontos = []
        indices = []
        #Mínimo de cada linha
        for i, dit in enumerate(self.dataset[1:], start=1):
            j = argmin(dit["distancias"])
            indices.append(j)
            pontos.append(dit["distancias"][j])

        i = np.argmin(np.array(pontos))
        j = indices[i]
        return i+1, j

    #Calcula a distância euclidiana
    def _distanciaEuclidiana(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    #Saída do arquivo
    def saidaArquivo(self, nomearquivo):
        nomearquivo = os.path.abspath("./saidaSingleLink/"+nomearquivo)
        #Cria um arquivo com o nome que foi passado como parâmetro
        #Supõem que o nome já tenha sido passado com a extensão .clu
        w = open(nomearquivo, 'w', encoding='utf-8')
        """
            Sendo o i o índice do elemento, verifica em qual cluster ele está,
            depois grava a linha com o identificador e o cluster.
        """
        for i, id in enumerate(self.ids):
            for j, dit in enumerate(self.dataset):
                if i in dit["cluster"]:
                    w.write(id+" "+str(j)+"\n")
                    break
            continue
        w.close()
    
    #Irá retornar a matriz
    #Saída da imagem
    def imagem(self):
        #Definindo um tamanho
        fig, ax = plt.subplots(figsize=(8, 4))
        #Para cada cluster
        for dit in self.dataset:
            #Pega os elementos do cluster e faz a transposição.
            ponto = self.pontos[dit["cluster"]].T
            #Espalha os pontos na imagem.
            ax.scatter(*ponto)

        #Título da imagem
        plt.title("K"+str(len(self.dataset)))
        #Exibe a imagem
        plt.show()

    def imprimir(self):
        print("------------------------------")
        for dit in self.dataset:
            aux = "["
            for ponto in dit["distancias"]:
                aux+=" "+str(ponto)
            print(aux+" ]\n")
        print("------------------------------")
    
    def imprimirCluster(self):
        print("------------------------------")
        for cluster, dit in enumerate(self.dataset):
            aux = str(cluster)+" ["
            for indice in dit["cluster"]:
                aux+=" "+str(indice)
            print(aux+" ]\n")
        print("------------------------------")

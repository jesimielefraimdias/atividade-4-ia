import os
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import silhouette_score


class IndiceRand:
    def __init__(self, saidaReal, saida):
        self.setSaidas(saidaReal, saida)

    def setSaidas(self, saidaReal, saida):
        self.setSaidaReal(saidaReal)
        self.setSaida(saida)

    def setSaidaReal(self, saidaReal):
        self.saidaReal = saidaReal

    def setSaida(self, saida):
        self.saida = saida

    def _openFile(self, nomearquivo):
        #Verifica-se o arquivo existe.
        if not os.path.isfile(nomearquivo):
            raise Exception("Arquivo "+nomearquivo+" não encontrado")
        #Se existe, abre em modo de leitura.
        return open(nomearquivo, "r", encoding="utf-8")
    
    def _getClusters(self, file):
        clusters = []
        
        for line in file:
            line = line.replace("\t",",").replace(" ",",").replace("\n","")
            line = line.split(",")
            if len(line) != 2:
                print(line)
                raise Exception("Erro no tratamento")
            clusters.append(line[1])

        return clusters

    def calARI(self):
        fileSaidaReal = self._getClusters(self._openFile(self.saidaReal))
        fileSaida = self._getClusters(self._openFile(self.saida))

        return adjusted_rand_score(fileSaidaReal, fileSaida)


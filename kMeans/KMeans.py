import matplotlib.pyplot as plt
import numpy as np
import os

class KMeans:
    def __init__(self, dataset, ids, kClusters=5, maxIteracoes=150, temSeed=True, seed=15):
        # Inicializa o número de cluster desejado.
        self.kClusters = kClusters
        # A quantidade máxima de iterações.
        self.maxIteracoes = maxIteracoes
        # Lista dos índices pertencentes a cada cluster
        self.clusters = [[] for _ in range(self.kClusters)]
        # Inicializa os centroids como uma lista vazia.
        self.centroides = []
        # Inicializa o dataset
        self.dataset = dataset
        # A identificação dos elementos (ou pontos)
        self.ids = ids
        #Inicializa o número de elemento e o número do atributo
        self.nElem, self.nAtri = dataset.shape
        """
            Ao ler o notebook, foi encontrado um seed com o valor de 15,
            logo, foi utilizado o seed por padrão 15.
            Caso realmente queira os valores randômicos, colocar temSeed como falso
        """
        if temSeed:
            np.random.seed(seed)

    def exec(self):
        """
        Pega aleatoriamente K índices que representam os K centróides no datasets
        sem repetições.
        """
        random_indeces = np.random.choice(self.nElem, self.kClusters, replace=False)
        #Com os índices dos centróides, pega o respectivo elemento no dataset
        self.centroides = [self.dataset[i] for i in random_indeces]

        """
            Agora executa a quantidade de iterações solicitada ou menos
            caso exista convergência entre o centroide novo e velho
        """
        for i in range(self.maxIteracoes):
           
            self.clusters = self._criarClusters()
            """
                guarda o valor do centróide antigo.
            """
            velhoCentroides = self.centroides
            self.centroides = self._recalcularCentroides()
            """
                Como otimização, pode-se verificar se os centróides
                não convergiram. Ou seja, se o centróide antigo não é igual ao novo,
                pois se ele for, não importa quantas interações ocorra, os centróides
                não irão mudar.
            """
            if sum([self._distanciaEuclidiana(velhoCentroides[i], self.centroides[i]) for i in range(self.kClusters)]) == 0:
                return i #retorna as i iterações
        return i #retorna as i iterações

    
    """
        Cria os clusters através dos centróides atuais.
        Cada elemento do cluster será um vetor que contém os índices dos
        elementos do dataset, ou seja, os índices que pertencem a este
        cluster.
    """
    def _criarClusters(self):
        #Inicializa uma variável para ser o cluster.
        clusters = [[] for _ in range(self.kClusters)]
        """
            Para cada elemento do dataset, verifica a qual centróide ele pertence.
            Após achar o centróide mais próximo do elemento, o seu índice é adicionado no
            respectivo cluster.
        """
        for i, elem in enumerate(self.dataset):
            clusters[self._centroidMaisProximo(elem)].append(i)
        
        #Retorna os novos clusters.
        return clusters

    #Calcula a distância euclidiana
    def _distanciaEuclidiana(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    #Retorna o índice do centróide mais próximo do elemento
    def _centroidMaisProximo(self, elem):
        """
        Calcula a distância euclidiana do elemento para o ponto no centróide
        e atribui o valor ao vetor para que seja possível usar a função argmin,
        que irá retornar o índice do menor valor.
        """
        #Depois, encontramos o elemento de menor distância e retornamos o seu index.
        return np.argmin([self._distanciaEuclidiana(elem, ponto) for ponto in self.centroides])

    #Recalcula os centróides
    def _recalcularCentroides(self):
        #Iniciaza os novos centróide como zero.
        centroides = np.zeros((self.kClusters, self.nAtri))
        """
            Irá executar o for K vezes sendo que o
            i será o índice desse cluster e o
            cluster terá os índices dos elementos de dataset.
        """
        for i, cluster in enumerate(self.clusters):
            """
                Usando a função np.mean, passando os parâmetros dataset
                que é um vetor de vetor de numpy.vector, com os índices desses clusters
                e o axis=0 será possível fazer o cálculo para atualizar os centróides.
            """
            novoCentroide = np.mean(self.dataset[cluster], axis=0)
            centroides[i] = novoCentroide
        #Retorna os centróides atualizado.
        return centroides

    #Saída do arquivo
    def saidaArquivo(self, nomearquivo):
        nomearquivo = os.path.abspath("./saidaKmeans/"+nomearquivo)
        #Cria um arquivo com o nome que foi passado como parâmetro
        #Supõem que o nome já tenha sido passado com a extensão .clu
        w = open(nomearquivo, 'w', encoding='utf-8')
        """
            Sendo o i o índice do elemento, verifica em qual cluster ele está,
            depois grava a linha com o identificador e o cluster.
        """
        for i, _ in enumerate(self.dataset):
            for j, cluster in enumerate(self.clusters):
                if i in cluster:
                    w.write(str(self.ids[i])+" "+str(j)+"\n")
                    break
            continue
        w.close()
    
    #Irá retornar a matriz
#    def getClusters()
    #Saída da imagem
    def imagem(self):
        #Definindo um tamanho
        fig, ax = plt.subplots(figsize=(12, 8))
        #Para cada cluster
        for _, index in enumerate(self.clusters):
            #Pega os elementos do cluster e faz a transposição.
            ponto = self.dataset[index].T
            #Espalha os pontos na imagem.
            ax.scatter(*ponto)
            
        #Faz o mesmo processo do for acima, porém para os centróides.
        for point in self.centroides:
            ax.scatter(*point, marker="*", color="black", linewidth=2)

        #Título da imagem
        plt.title("K"+str(self.kClusters))

        #Exibe a imagem
        plt.show()
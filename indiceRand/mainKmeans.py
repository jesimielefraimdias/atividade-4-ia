from IndiceRand import IndiceRand
import os

#printando os ARI do globulars
globularsReal = os.path.abspath("datasets/c2ds3-2gReal.clu")
globularsK2 = os.path.abspath("../kMeans/saidaKmeans/globulars/k2.clu")
globularsK3 = os.path.abspath("../kMeans/saidaKmeans/globulars/k3.clu")
globularsK4 = os.path.abspath("../kMeans/saidaKmeans/globulars/k4.clu")
globularsK5 = os.path.abspath("../kMeans/saidaKmeans/globulars/k5.clu")

indiceRand = IndiceRand(globularsReal, globularsK2)
print("\nK-Means - IRA")
print("GLOBULARS")
print("IRA K2 = "+str(indiceRand.calARI()))

indiceRand.setSaida(globularsK3)
print("IRA K3 = "+str(indiceRand.calARI()))

indiceRand.setSaida(globularsK4)
print("IRA K4 = "+str(indiceRand.calARI()))

indiceRand.setSaida(globularsK5)
print("IRA K5 = "+str(indiceRand.calARI()))

#printando os ARI do spirals
spiralsReal = os.path.abspath("datasets/c2ds1-2spReal.clu")
spiralsK2 = os.path.abspath("../kMeans/saidaKmeans/spirals/k2.clu")
spiralsK3 = os.path.abspath("../kMeans/saidaKmeans/spirals/k3.clu")
spiralsK4 = os.path.abspath("../kMeans/saidaKmeans/spirals/k4.clu")
spiralsK5 = os.path.abspath("../kMeans/saidaKmeans/spirals/k5.clu")

indiceRand = IndiceRand(spiralsReal, spiralsK2)
print("\nSPIRALS")
print("IRA K2 = "+str(indiceRand.calARI()))

indiceRand.setSaida(spiralsK3)
print("IRA K3 = "+str(indiceRand.calARI()))

indiceRand.setSaida(spiralsK4)
print("IRA K4 = "+str(indiceRand.calARI()))

indiceRand.setSaida(spiralsK5)
print("IRA K5 = "+str(indiceRand.calARI()))

#printando os ARI do monkey
monkeyReal = os.path.abspath("datasets/monkeyReal1.clu")
monkeyK5 = os.path.abspath("../kMeans/saidaKmeans/monkey/k5.clu")
monkeyK6 = os.path.abspath("../kMeans/saidaKmeans/monkey/k6.clu")
monkeyK7 = os.path.abspath("../kMeans/saidaKmeans/monkey/k7.clu")
monkeyK8 = os.path.abspath("../kMeans/saidaKmeans/monkey/k8.clu")
monkeyK9 = os.path.abspath("../kMeans/saidaKmeans/monkey/k9.clu")
monkeyK10 = os.path.abspath("../kMeans/saidaKmeans/monkey/k10.clu")
monkeyK11 = os.path.abspath("../kMeans/saidaKmeans/monkey/k11.clu")
monkeyK12 = os.path.abspath("../kMeans/saidaKmeans/monkey/k12.clu")

indiceRand = IndiceRand(monkeyReal, monkeyK5)
print("\nMONKEY")
print("IRA K5 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK6)
print("IRA K6 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK7)
print("IRA K7 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK8)
print("IRA K8 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK9)
print("IRA K9 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK10)
print("IRA K10 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK11)
print("IRA K11 = "+str(indiceRand.calARI()))

indiceRand.setSaida(monkeyK12)
print("IRA K12 = "+str(indiceRand.calARI()))
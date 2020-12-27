# NOMÉS TROBA CAMINS SIMPLES (NO REPETEIX NODES)
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import re

G = nx.Graph()
G.add_weighted_edges_from([[1, 2, 82],
 [2, 21, 64],
 [21, 22, 180],
 [22, 24, 160],
 [24, 100, 22],
 [2, 3, 140],
 [3, 21, 90],
 [3, 4, 32],
 [3, 20, 75],
 [4, 20, 86],
 [4, 5, 56],
 [5, 6, 300],
 [20, 18, 71],
 [5, 18, 50],
 [20, 23, 46],
 [22, 23, 81],
 [23, 24, 150],
 [6, 13, 24],
 [13, 14, 24],
 [6, 7, 28],
 [6, 11, 99],
 [7, 9, 43],
 [7, 8, 34],
 [8, 9, 10],
 [9, 9, 120],
 [9, 11, 97],
 [8, 11, 49],
 [11, 12, 150],
 [13, 15, 86],
 [14, 16, 86],
 [12, 15, 75],
 [12, 16, 300],
 [16, 17, 41],
 [17, 19, 65],
 [19, 23, 61],
 [17, 18, 71]])

camins = list(nx.all_simple_paths(G, 1, 100))

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')

def grafica_graf(G):
	nx.draw_networkx(G, pos)
	nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
	plt.show()

def f(cami):
	s = 0
	for nVertex in range(len(cami)-1):
		s += labels.get((cami[nVertex],cami[nVertex+1]), labels.get((cami[nVertex+1],cami[nVertex])))
	return s

pesos_camins = list(map(f, camins))
longitud_maxima = max(pesos_camins)
iCami_mes_llarg = pesos_camins.index(longitud_maxima)
Cami_mes_llarg = camins[iCami_mes_llarg]
print(Cami_mes_llarg)

grafica_graf(G)
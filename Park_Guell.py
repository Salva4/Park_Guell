import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import re
import heapq as hq

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

nodes = list(G.nodes())
edges = list(G.edges())
labels = nx.get_edge_attributes(G, 'weight')


def pes(i, j):
	return labels.get((i, j), labels.get((j, i)))

def f(cami):
	s = 0
	for nVertex in range(len(cami)-1):
		s += pes(cami[nVertex], cami[nVertex+1])
	return s

def grafica_graf(G):
	pos = nx.spring_layout(G)
	labels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx(G, pos)
	nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
	plt.show()

def ajunta(n1, nELIMINAR, n2):
	pes1 = pes(n1, nELIMINAR)
	pes2 = pes(nELIMINAR, n2)
	G.add_weighted_edges_from([[n1, n2, pes1+pes2]])
	G.remove_node(nELIMINAR)

# FALLA: 23 -> 19 -> 23.1 !!
def duplica_nodes(G): # requeriment: màxim de veïns d'un node en tot el graf: 5. (màxim actual: 4). Es compleix :)
	global labels
	nodes_a_modificar = []
	for node in nodes:
		veins = list(G.neighbors(node))
		if len(veins) >= 4:
			nodes_a_modificar.append(node)

	for node in nodes_a_modificar:
		veins = list(G.neighbors(node))
		nou_node = node + .1
		G.add_weighted_edges_from([[node, nou_node, 0]])
		G.add_weighted_edges_from([[nou_node, vei, pes(node, vei)] for vei in veins])
		labels = nx.get_edge_attributes(G, 'weight')

def camiMesLlarg(G, node_i, node_f):
	duplica_nodes(G)
	camins = list(nx.all_simple_paths(G, node_i, node_f))
	pesos_camins = list(map(f, camins))
	longitud_maxima = max(pesos_camins)
	iCami_mes_llarg = pesos_camins.index(longitud_maxima)
	cami_mes_llarg = camins[iCami_mes_llarg]
	return cami_mes_llarg


'''# Elimina nodes innecessaris: 1, 100, 14, 15, 19. Total de nodes: 19.
long1_2 = pes(1, 2)
long24_100 = pes(24, 100)
G.remove_edges_from([(1, 2), (24, 100)])
ajunta(13, 14, 16)
ajunta(13, 15, 12)
ajunta(17, 19, 23)
labels = nx.get_edge_attributes(G, 'weight')'''


# Troba tots els camins que no repeteixin aresta ----> Hauria de cercar-ho als apunts d'algorísmia!!!
cami_mes_llarg = camiMesLlarg(G, 1, 100)
print(cami_mes_llarg)

grafica_graf(G)

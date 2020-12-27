import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import re
import heapq as hq
import sys

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


def pes(G, i, j):
	labels = nx.get_edge_attributes(G, 'weight')
	return labels.get((i, j), labels.get((j, i)))

def f(t):
	cami = t[0]
	G = t[1]
	s = 0
	for nVertex in range(len(cami)-1):
		s += pes(G, cami[nVertex], cami[nVertex+1])
	return s

def grafica_graf(G):
	pos = nx.spring_layout(G)
	labels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx(G, pos)
	nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
	plt.show()

def duplica_graf(G):
	S = set()
	nodes_a_dividir = [3, 20, 6, 23, 11, 9]
	for i1 in range(3):
		for i2 in range(3):
			for i3 in range(3):
				for i4 in range(3):
					for i5 in range(3):
						for i6 in range(3):
							H = G.copy()
							I = [i1, i2, i3, i4, i5, i6]
							for iNode in range(len(nodes_a_dividir)):
								node = nodes_a_dividir[iNode]
								veins = list(H.neighbors(node))
								if I[iNode] == 0:
									x, y = 2, 3
								elif I[iNode] == 1:
									x, y = 1, 3
								elif I[iNode] == 2:
									x, y = 1, 2
								else:
									error()
								wx = pes(H, node, veins[x])
								#print(wx)
								wy = pes(H, node, veins[y])
								H.remove_edge(node, veins[x])
								H.remove_edge(node, veins[y])
								nou_node = node + .1;
								H.add_weighted_edges_from([[nou_node, veins[x], wx], [nou_node, veins[y], wy]])
							S.add(H)
	return S

def camiMesLlarg(S, node_i, node_f):
	#duplica_nodes(G)
	cami_mes_llarg = None
	m = 0
	while len(S) > 0:
		G = S.pop()
		camins = list(nx.all_simple_paths(G, node_i, node_f))
		input_camins = [(cami, G) for cami in camins]
		pesos_camins = list(map(f, input_camins))
		longitud_maxima = max(pesos_camins)
		if longitud_maxima > m:
			m = longitud_maxima
			iCami_mes_llarg = pesos_camins.index(longitud_maxima)
			cami_mes_llarg = camins[iCami_mes_llarg]
	return cami_mes_llarg, m

def error():
	print("ERROR")
	sys.exit


S = duplica_graf(G)
cami_mes_llarg, longitud_maxima = camiMesLlarg(S, 1, 100)
print(cami_mes_llarg, longitud_maxima)

#grafica_graf(G)

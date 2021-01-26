import networkx as nx
import matplotlib.pyplot as plt
import time

t0 = time.time()

itmax = 0

edges = [[1, 2, 82],
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
		 [17, 18, 71]]

G = nx.Graph()
G.add_weighted_edges_from(edges)

def dibuixa(G):
	pos=nx.spring_layout(G) 
	nx.draw_networkx(G, pos)
	labels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
	plt.show()

def calcula_valor_cami(cami):
	#print(f"cami: {cami}")
	labels = nx.get_edge_attributes(G, 'weight')
	#print(f"labels: {labels}")
	suma = 0
	for i in range(len(cami) - 1):
		suma += labels.get((cami[i], cami[i+1]), labels.get((cami[i+1], cami[i]), "error"))
	return suma

def aslotuyo(G):
	cami_mes_curt = nx.shortest_path(G, 1, 100)
	valor = calcula_valor_cami(cami_mes_curt)
	return cami_mes_curt, valor

cami_mes_curt, valor = aslotuyo(G)
print(cami_mes_curt, valor)

maxVal = (cami_mes_curt, valor)

it = 0
Gs = [G]
arestes_analitzades = []
while Gs != [] and maxVal[1] < 1900: #it < itmax:
	g = Gs.pop(0)
	arestes = str(list(g.edges))
	if arestes not in arestes_analitzades:
		arestes_analitzades.append(arestes)
		cmc = nx.shortest_path(g, 1, 100)
		vlr = calcula_valor_cami(cmc)
		if vlr > maxVal[1]:
			maxVal = (cmc, vlr)

		for i in range(len(cmc)-1):
			Gc = g.copy()
			Gc.remove_edge(cmc[i], cmc[i+1])
			if nx.has_path(Gc, 1, 100):
				Gs.append(Gc)

	it += 1

print(maxVal[0], maxVal[1])
print(f"time: {time.time() - t0}")
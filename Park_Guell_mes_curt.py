import numpy as np 
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

# Modificat: 11 -> 10, ... , 24 -> 23; i 100 -> 24
edges = [[0, 1, 82], 
         [1, 19, 64], 
         [19, 20, 180], 
         [20, 22, 160], 
         [22, 23, 22], 
         [1, 2, 140], 
         [2, 19, 90], 
         [2, 3, 32], 
         [2, 18, 75], 
         [3, 18, 86], 
         [3, 4, 56], 
         [4, 5, 300], 
         [18, 16, 71], 
         [4, 16, 50], 
         [18, 21, 46], 
         [20, 21, 81], 
         [21, 22, 150], 
         [5, 11, 24], 
         [11, 12, 24], 
         [5, 6, 28], 
         [5, 9, 99], 
         [6, 8, 43], 
         [6, 7, 34], 
         [7, 8, 10], 
         [8, 8, 120], 
         [8, 9, 97], 
         [7, 9, 49], 
         [9, 10, 150], 
         [11, 13, 86], 
         [12, 14, 86], 
         [10, 13, 75], 
         [10, 14, 300], 
         [14, 15, 41], 
         [15, 17, 65], 
         [17, 21, 61], 
         [15, 16, 71]]

nodes = [i for i in range(1, 10)] + [i for i in range(11, 25)] + [100]
n = len(nodes)
matriu_arestes = np.zeros([n, n])

for i,j,v in edges:
	x = min(i, j)
	y = max(i, j)
	matriu_arestes[x, y] = v

graph = csr_matrix(matriu_arestes)
#print(graph)

dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=0, return_predecessors=True)
print(dist_matrix)
print(predecessors)
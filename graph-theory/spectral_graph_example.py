"""
Spectral graph theory: eigenvalues of Laplacian
"""
import networkx as nx
import numpy as np

G = nx.path_graph(5)
L = nx.laplacian_matrix(G).todense()
evals = np.linalg.eigvals(L)
print("Laplacian eigenvalues:", evals)

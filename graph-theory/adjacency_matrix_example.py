"""
Adjacency matrix and Laplacian of a simple graph
"""
import numpy as np
import networkx as nx

G = nx.cycle_graph(4)
A = nx.adjacency_matrix(G).todense()
L = nx.laplacian_matrix(G).todense()
print("Adjacency matrix:\n", A)
print("Laplacian matrix:\n", L)

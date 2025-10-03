"""
Application: Node classification with a simple Graph Neural Network (GNN)
"""
import networkx as nx
import numpy as np

# Simple graph and features
G = nx.karate_club_graph()
A = nx.adjacency_matrix(G).todense()
X = np.eye(G.number_of_nodes())
W = np.random.randn(G.number_of_nodes(), 2)

# Simple GNN layer: X' = AXW
X_new = A @ X @ W
print("Node embeddings (first 5):\n", X_new[:5])

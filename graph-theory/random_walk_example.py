"""
Random walk on a graph
"""
import networkx as nx
import numpy as np

G = nx.cycle_graph(5)
P = nx.to_numpy_array(G) / 2  # Each node has degree 2
state = 0
walk = [state]
for _ in range(10):
    neighbors = list(G.neighbors(state))
    state = np.random.choice(neighbors)
    walk.append(state)
print("Random walk:", walk)

"""
Application: Symmetry and equivariant neural networks
"""
import numpy as np

def equivariant_layer(x):
    # Example: rotation equivariant layer for 2D input
    theta = np.pi/4
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return R @ x

x = np.array([1.0, 0.0])
print("Original:", x)
print("After equivariant layer:", equivariant_layer(x))

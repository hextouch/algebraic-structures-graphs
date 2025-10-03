"""
Lie algebra: so(2) - skew-symmetric matrices
"""
import numpy as np

def so2_algebra():
    return np.array([[0, -1], [1, 0]])

print("so(2) generator:")
print(so2_algebra())

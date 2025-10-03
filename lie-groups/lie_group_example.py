"""
Lie group: SO(2) - rotations in the plane
"""
import numpy as np

def so2(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

print("SO(2) rotation by pi/4:")
print(so2(np.pi/4))

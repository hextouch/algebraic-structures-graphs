"""
Combinatorics: number of combinations (n choose k)
"""
import math

def n_choose_k(n, k):
    return math.comb(n, k)

print("5 choose 2:", n_choose_k(5, 2))

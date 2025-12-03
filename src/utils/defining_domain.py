import numpy as np

def auto_domain(max_extent, N=80, margin=0.3):
    L = max_extent + margin
    axis = np.linspace(-L, L, N)
    return np.meshgrid(axis, axis, axis, indexing='ij')

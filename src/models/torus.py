# Generates a torus from inner and outer radius. An optional origin parameter sets its position.

import numpy as np

def create_torus(inner_radius, outer_radius, origin=(0, 0, 0)):
    if inner_radius <= 0 or outer_radius <= 0:
        raise ValueError("Radii must be positive numbers.")

    ox, oy, oz = origin
    resolution = 5

    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, 2 * np.pi, resolution)
    u, v = np.meshgrid(u, v)

    x = (outer_radius + inner_radius * np.cos(v)) * np.cos(u) + ox
    y = (outer_radius + inner_radius * np.cos(v)) * np.sin(u) + oy
    z = inner_radius * np.sin(v) + oz

    vertices = []
    for i in range(resolution):
        for j in range(resolution):
            vertices.append((x[i, j], y[i, j], z[i, j]))

    edges = []
    for i in range(resolution):
        for j in range(resolution):
            a = i * resolution + j
            b = i * resolution + ((j + 1) % resolution)
            c = ((i + 1) % resolution) * resolution + j
            edges.append((a, b))
            edges.append((a, c))

    return vertices, edges

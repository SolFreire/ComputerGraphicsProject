import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# from defining_domain import auto_domain

def create_torus(inner_radius, outer_radius, resolution=17, origin=(0, 0, 0)):
    if inner_radius <= 0 or outer_radius <= 0:
        raise ValueError("Radii must be positive numbers.")

    ox, oy, oz = origin

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

def plot_torus(ax, vertices, resolution=17):
    v = np.array(vertices)

    triangles = []

    for i in range(resolution):
        for j in range(resolution):
            a = i * resolution + j
            b = i * resolution + ((j + 1) % resolution)
            c = ((i + 1) % resolution) * resolution + ((j + 1) % resolution)
            d = ((i + 1) % resolution) * resolution + j

            triangles.append([v[a], v[b], v[c]])
            triangles.append([v[a], v[c], v[d]])

    mesh = Poly3DCollection(triangles, facecolor="yellow", edgecolor="black", alpha=1)
    ax.add_collection3d(mesh)

# def implicit_torus(R, r, N=80):
#     max_extent = R + r
#     X, Y, Z = auto_domain(max_extent, N=N)

#     F = (np.sqrt(X**2 + Y**2) - R)**2 + Z**2 - r**2
#     return F


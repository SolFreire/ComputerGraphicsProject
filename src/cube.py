import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_cube(side_length, origin=(0, 0, 0)):
    if side_length <= 0:
        raise ValueError("side_length must be a positive number.")

    ox, oy, oz = origin
    half = side_length / 2

    vertices = [
        (ox - half, oy - half, oz - half),
        (ox + half, oy - half, oz - half),
        (ox + half, oy + half, oz - half),
        (ox - half, oy + half, oz - half),
        (ox - half, oy - half, oz + half),
        (ox + half, oy - half, oz + half),
        (ox + half, oy + half, oz + half),
        (ox - half, oy + half, oz + half),
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    faces = [
        (0,1,2,3),
        (4,7,6,5),
        (0,4,5,1),
        (3,2,6,7),
        (1,5,6,2),
        (0,3,7,4),
    ]

    return vertices, edges, faces

def plot_cube(ax, vertices):
    v = np.array(vertices)

    triangles = [
        [v[0], v[1], v[2]], [v[0], v[2], v[3]],
        [v[4], v[5], v[6]], [v[4], v[6], v[7]],
        [v[0], v[1], v[5]], [v[0], v[5], v[4]],
        [v[2], v[3], v[7]], [v[2], v[7], v[6]],
        [v[1], v[2], v[6]], [v[1], v[6], v[5]],
        [v[4], v[7], v[3]], [v[4], v[3], v[0]]
    ]

    mesh = Poly3DCollection(triangles, facecolor="cyan", edgecolor="black", alpha=1)
    ax.add_collection3d(mesh)

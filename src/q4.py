import matplotlib.pyplot as plt

from cube import *
from torus import *
from pipe import *
from common import *

def project_vertices(vertices):
    new_vertices = []

    for x, y, z in vertices:
        if z == 0:
            z = 1e-6

        xp = x / z
        yp = y / z
        new_vertices.append((xp, yp))

    return new_vertices

def plot_solid_2d(ax, vertices_2d, edges, color):
    for a, b in edges:
        x1, y1 = vertices_2d[a]
        x2, y2 = vertices_2d[b]
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)

fig, ax = plt.subplots(figsize=(6, 6))

cube_vertices, cube_edges, _, torus_vertices, torus_edges, _, pipe_vertices, pipe_edges, _ = get_polys()

RT = perspective_matrix()

cube_vertices = transform(cube_vertices, RT)
torus_vertices = transform(torus_vertices, RT)
pipe_vertices = transform(pipe_vertices, RT)

cube_2d = project_vertices(cube_vertices)
torus_2d = project_vertices(torus_vertices)
pipe_2d = project_vertices(pipe_vertices)

plot_solid_2d(ax, cube_2d, cube_edges, color="cyan")
plot_solid_2d(ax, torus_2d, torus_edges, color="yellow")
plot_solid_2d(ax, pipe_2d, pipe_edges, color="magenta")

ax.set_aspect("equal")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.invert_xaxis()
ax.grid(True)

plt.show()

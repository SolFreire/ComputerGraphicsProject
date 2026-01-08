import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from cube import *
from torus import *
from pipe import *
from common import *

import matplotlib.colors as mcolors

def darken_color(color, factor=0.7):
    r, g, b = mcolors.to_rgb(color)
    return (r * factor, g * factor, b * factor)

def project_vertices(vertices):
    new_vertices = []

    for x, y, z in vertices:
        if z == 0:
            z = 1e-6

        xp = x / z
        yp = y / z
        new_vertices.append((xp, yp))

    return new_vertices

def collect_faces(vertices_3d, vertices_2d, faces, color):
    face_data = []

    for face in faces:
        z_avg = sum(vertices_3d[i][2] for i in face) / len(face)
        poly_2d = [vertices_2d[i] for i in face]

        face_data.append({
            "z": z_avg,
            "poly": poly_2d,
            "color": color
        })

    return face_data

fig, ax = plt.subplots(figsize=(6, 6))

cube_vertices, _, cube_faces, torus_vertices, _, torus_faces, pipe_vertices, _, pipe_faces = get_polys()

RT = perspective_matrix()

pipe_vertices = transform(pipe_vertices, RT)
torus_vertices = transform(torus_vertices, RT)
cube_vertices = transform(cube_vertices, RT)

pipe_2d = project_vertices(pipe_vertices)
torus_2d = project_vertices(torus_vertices)
cube_2d = project_vertices(cube_vertices)

all_faces = []

all_faces += collect_faces(pipe_vertices, pipe_2d, pipe_faces, "magenta")
all_faces += collect_faces(torus_vertices, torus_2d, torus_faces, "yellow")
all_faces += collect_faces(cube_vertices, cube_2d, cube_faces, "cyan")

all_faces.sort(key=lambda f: f["z"], reverse=True)

for face in all_faces:
    patch = Polygon(
        face["poly"],
        closed=True,
        facecolor=face["color"],
        edgecolor=darken_color(face["color"], 0.5),
        alpha=1
    )
    ax.add_patch(patch)

ax.set_aspect("equal")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.invert_xaxis()
ax.grid(True)

plt.show()

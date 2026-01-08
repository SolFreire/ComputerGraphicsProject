import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from cube import *
from torus import *
from pipe import *
from common import *

def face_normal(v0, v1, v2):
    a = np.array(v1) - np.array(v0)
    b = np.array(v2) - np.array(v0)
    return np.cross(a, b)


def is_face_front(vertices, face):
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]

    n = face_normal(v0, v1, v2)

    view = -np.array(v0)

    return np.dot(n, view) > 0

def build_edge_face_map(faces):
    edge_faces = defaultdict(list)

    for fi, face in enumerate(faces):
        for i in range(len(face)):
            a = face[i]
            b = face[(i + 1) % len(face)]
            edge = tuple(sorted((a, b)))
            edge_faces[edge].append(fi)

    return edge_faces

def visible_edges(vertices, faces):
    face_visible = [
        is_face_front(vertices, face)
        for face in faces
    ]

    edge_faces = build_edge_face_map(faces)
    visible = set()

    for edge, fs in edge_faces.items():
        if any(face_visible[f] for f in fs):
            visible.add(edge)

    return visible

def project_vertices(vertices):
    result = []

    for x, y, z in vertices:
        if z == 0:
            z = 1e-6
        result.append((x / z, y / z))

    return result

def collect_visible_edges(vertices_3d, vertices_2d, faces, color):
    edges = visible_edges(vertices_3d, faces)
    data = []

    for a, b in edges:
        z_avg = (vertices_3d[a][2] + vertices_3d[b][2]) / 2

        data.append({
            "z": z_avg,
            "p1": vertices_2d[a],
            "p2": vertices_2d[b],
            "color": color
        })

    return data

fig, ax = plt.subplots(figsize=(6, 6))

cube_vertices, _, cube_faces, torus_vertices, _, torus_faces, pipe_vertices, _, pipe_faces = get_polys()

RT = perspective_matrix()

pipe_vertices = transform(pipe_vertices, RT)
torus_vertices = transform(torus_vertices, RT)
cube_vertices = transform(cube_vertices, RT)

pipe_2d = project_vertices(pipe_vertices)
torus_2d = project_vertices(torus_vertices)
cube_2d = project_vertices(cube_vertices)

all_edges = []

all_edges += collect_visible_edges(cube_vertices, cube_2d, cube_faces, "cyan")
all_edges += collect_visible_edges(torus_vertices, torus_2d, torus_faces, "yellow")
all_edges += collect_visible_edges(pipe_vertices, pipe_2d, pipe_faces, "magenta")

all_edges.sort(key=lambda e: e["z"], reverse=True)

for e in all_edges:
    ax.plot(
        [e["p1"][0], e["p2"][0]],
        [e["p1"][1], e["p2"][1]],
        color=e["color"],
        linewidth=1.8
    )

ax.set_aspect("equal")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.grid(True)

plt.show()

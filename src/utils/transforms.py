import numpy as np

import numpy as np

def scale(vertices, sx, sy, sz):
    S = np.array([
        [sx, 0,  0 ],
        [0,  sy, 0 ],
        [0,  0,  sz]
    ])

    v = np.array(vertices, dtype=float)
    center = v.mean(axis=0)
    v0 = v - center

    new_vertices = v0 @ S.T
    new_vertices += center

    return new_vertices

def translate(vertices, tx, ty, tz):
    T = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ])

    new_vertices = []

    for vx, vy, vz in vertices:
        v = np.array([vx, vy, vz, 1])
        v_new = T @ v
        new_vertices.append((v_new[0], v_new[1], v_new[2]))

    return new_vertices

import numpy as np

def transform(vertices, T):
    new_vertices = []

    for vx, vy, vz in vertices:
        v = np.array([vx, vy, vz, 1])
        v_new = T @ v
        new_vertices.append((v_new[0], v_new[1], v_new[2]))

    return new_vertices

def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ])

def translate(vertices, tx, ty, tz):
    T = translation_matrix(tx, ty, tz)

    return transform(vertices, T)

def scale_matrix(sx, sy, sz):
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def scale(vertices, sx, sy, sz):
    v = np.array(vertices, dtype=float)
    center = v.mean(axis=0)

    T1 = translation_matrix(-center[0], -center[1], -center[2])
    S  = scale_matrix(sx, sy, sz)
    T2 = translation_matrix(center[0], center[1], center[2])

    M = T2 @ S @ T1

    return transform(vertices, M)

def rotation_matrix_x(alpha):
    c = np.cos(alpha)
    s = np.sin(alpha)

    return np.array([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]
    ])

def rotation_matrix_y(alpha):
    c = np.cos(alpha)
    s = np.sin(alpha)

    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
    ])

def rotation_matrix_z(alpha):
    c = np.cos(alpha)
    s = np.sin(alpha)

    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

def rotate(vertices, angle_deg, axis):
    angle = np.deg2rad(angle_deg)

    v = np.array(vertices, dtype=float)
    center = v.mean(axis=0)

    if axis.lower() == 'x':
        R = rotation_matrix_x(angle)
    elif axis.lower() == 'y':
        R = rotation_matrix_y(angle)
    elif axis.lower() == 'z':
        R = rotation_matrix_z(angle)
    else:
        raise ValueError("o parâmetro axis deve ser 'x', 'y' ou 'z'")

    T1 = translation_matrix(-center[0], -center[1], -center[2])
    T2 = translation_matrix( center[0],  center[1],  center[2])

    M = T2 @ R @ T1

    return transform(vertices, M)

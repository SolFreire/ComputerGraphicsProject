from cube import *
from torus import *
from pipe import *
from transforms import *

def get_polys():
    cube_vertices, cube_edges, cube_faces = create_cube(4)
    cube_vertices = translate(cube_vertices, 3, 0, 5)

    torus_vertices, torus_edges, torus_faces = create_torus(1, 2)
    torus_vertices = rotate(torus_vertices, 45, 'x')

    control_points = [
        (-5, 0, -2),
        (-5, -2, 2),
        (4, 16, 8),
        (4, 16, 8)
    ]
    pipe_vertices, pipe_edges, pipe_faces = create_pipe(control_points)
    pipe_vertices = scale(pipe_vertices, 2, 2, 2)

    return (
        cube_vertices, cube_edges, cube_faces,
        torus_vertices, torus_edges, torus_faces,
        pipe_vertices, pipe_edges, pipe_faces
    )

def perspective_matrix():
    eye = np.array([0, 0, -8])
    at = np.array([0, 0, 0])

    z = at - eye
    z = z / np.linalg.norm(z)

    up = np.array([0, 1, 0])

    if abs(np.dot(up, z)) > 0.99:
        up = np.array([0, 0, -1])

    x = np.cross(up, z)
    x = x / np.linalg.norm(x)

    y = np.cross(z, x)

    R = np.array([
        [x[0], x[1], x[2], 0],
        [y[0], y[1], y[2], 0],
        [z[0], z[1], z[2], 0],
        [0,    0,    0,    1]
    ])

    T = np.array([
        [1, 0, 0, -eye[0]],
        [0, 1, 0, -eye[1]],
        [0, 0, 1, -eye[2]],
        [0, 0, 0, 1]
    ])

    return R @ T

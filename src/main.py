import matplotlib.pyplot as plt

from utils.transforms import *

from models.cube import *
from models.torus import *
from models.pipe import *

def get_polys():
    cube_vertices, cube_edges = create_cube(4)
    cube_vertices = translate(cube_vertices, 4, 0, 4)

    torus_vertices, torus_edges = create_torus(1, 2)

    control_points = [
        (-5, 0, -2),
        (-5, -2, 2),
        (4, 16, 8),
        (4, 16, 8)
    ]
    pipe_vertices, pipe_edges = create_pipe(control_points)
    pipe_vertices = scale(pipe_vertices, 2, 2, 2)

    return cube_vertices, cube_edges, torus_vertices, torus_edges, pipe_vertices, pipe_edges

def questao_2():
    # Cria figura e eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cube_vertices, cube_edges, torus_vertices, torus_edges, pipe_vertices, pipe_edges = get_polys()

    plot_cube(ax, cube_vertices)
    plot_torus(ax, torus_vertices)
    plot_pipe(ax, pipe_vertices)

    ax.set_xlim([-8, 8])
    ax.set_ylim([-8, 8])
    ax.set_zlim([-8, 8])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

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

def plot_camera_frustum(ax,
    z_near=0.1,
    z_far=1.0,
    near_size=0.05,
    far_size=0.4,
    color="red",
    alpha=0.25
):
    n = near_size
    zn = z_near
    near = np.array([
        [-n, -n, zn],
        [ n, -n, zn],
        [ n,  n, zn],
        [-n,  n, zn],
    ])

    f = far_size
    zf = z_far
    far = np.array([
        [-f, -f, zf],
        [ f, -f, zf],
        [ f,  f, zf],
        [-f,  f, zf],
    ])

    faces = [
        near,
        far,
        [near[0], near[1], far[1], far[0]],
        [near[1], near[2], far[2], far[1]],
        [near[2], near[3], far[3], far[2]],
        [near[3], near[0], far[0], far[3]],
    ]

    frustum = Poly3DCollection(faces, facecolor=color, edgecolor="black", alpha=alpha)
    ax.add_collection3d(frustum)

def questao_3():
    # Cria figura e eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cube_vertices, cube_edges, torus_vertices, torus_edges, pipe_vertices, pipe_edges = get_polys()

    RT = perspective_matrix()

    cube_vertices = transform(cube_vertices, RT)
    torus_vertices = transform(torus_vertices, RT)
    pipe_vertices = transform(pipe_vertices, RT)

    plot_cube(ax, cube_vertices)
    plot_torus(ax, torus_vertices)
    plot_pipe(ax, pipe_vertices)

    ax.scatter(0, 0, 0, s=30, color="black", depthshade=True)
    plot_camera_frustum(ax)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

def plot_solid_2d(ax, vertices_2d, edges, color):
    for a, b in edges:
        x1, y1 = vertices_2d[a]
        x2, y2 = vertices_2d[b]
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)

def questao_4():
    fig, ax = plt.subplots(figsize=(6, 6))

    cube_vertices, cube_edges, torus_vertices, torus_edges, pipe_vertices, pipe_edges = get_polys()

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

# questao_2()
questao_3()
# questao_4()

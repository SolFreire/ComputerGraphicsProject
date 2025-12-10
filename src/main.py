import matplotlib.pyplot as plt

from utils.transforms import *

from models.cube import *
from models.torus import *
from models.pipe import *

def questao_2():
    # Cria figura e eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cube_vertices, cube_edges = create_cube(4)
    cube_vertices = translate(cube_vertices, 4, 0, 4)

    torus_vertices, torus_edges = create_torus(1, 2)

    control_points = [
        (0, 0, -3),
        (1, 2, 1),
        (-1, -2, -1),
        (0, 0, 3)
    ]
    pipe_vertices, pipe_edges = create_pipe(control_points)
    pipe_vertices = translate(pipe_vertices, -5, 0, 0)
    pipe_vertices = scale(pipe_vertices, 2, 2, 2)

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

def questao_3():
    # Cria figura e eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cube_vertices, cube_edges = create_cube(4)
    cube_vertices = translate(cube_vertices, 4, 0, 4)

    torus_vertices, torus_edges = create_torus(1, 2)

    control_points = [
        (0, 0, -3),
        (1, 2, 1),
        (-1, -2, -1),
        (0, 0, 3)
    ]
    pipe_vertices, pipe_edges = create_pipe(control_points)
    pipe_vertices = translate(pipe_vertices, -5, 0, 0)
    pipe_vertices = scale(pipe_vertices, 2, 2, 2)

    # ax.set_xlim([-8, 8])
    # ax.set_ylim([-8, 8])
    # ax.set_zlim([-8, 8])

    eye = np.array([8, 0, 0])
    at = np.array([0, 0, 0])

    z = at - eye
    z = z / np.linalg.norm(z)

    up = np.array([0, 1, 0])
    # Se z e up estão quase paralelos, troca up
    if abs(np.dot(up, z)) > 0.99:
        up = np.array([1, 0, 0])

    x = np.cross(up, z)
    x = x / np.linalg.norm(x)

    y = np.cross(z, x)

    R = np.array([
        [x[0], y[0], z[0], 0],
        [x[1], y[1], z[1], 0],
        [x[2], y[2], z[2], 0],
        [0,    0,    0,    1]
    ])
    print(R)

    T = np.array([
        [1, 0, 0, -eye[0]],
        [0, 1, 0, -eye[1]],
        [0, 0, 1, -eye[2]],
        [0, 0, 0, 1]
    ])
    RT = R @ T

    cube_vertices = transform(cube_vertices, RT)
    torus_vertices = transform(torus_vertices, RT)
    pipe_vertices = transform(pipe_vertices, RT)

    plot_cube(ax, cube_vertices)
    plot_torus(ax, torus_vertices)
    plot_pipe(ax, pipe_vertices)

    ax.scatter(0, 0, 0, s=20, color="black", depthshade=True)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

# questao_2()
questao_3()

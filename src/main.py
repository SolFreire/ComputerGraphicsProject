import matplotlib.pyplot as plt

from utils.transforms import *

from models.cube import *
from models.torus import *
from models.pipe import *

# Cria figura e eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube_vertices, cube_edges = create_cube(4)
cube_vertices = translate(cube_vertices, 4, 0, 4)
plot_cube(ax, cube_vertices)

torus_vertices, torus_edges = create_torus(1, 2)
plot_torus(ax, torus_vertices)


control_points = [
    (0, 0, -3),
    (1, 2, 1),
    (-1, -2, -1),
    (0, 0, 3)
]
pipe_vertices, pipe_edges = create_pipe(control_points)
pipe_vertices = translate(pipe_vertices, -5, 0, 0)
pipe_vertices = scale(pipe_vertices, 2, 2, 2)

plot_pipe(ax, pipe_vertices)

ax.set_xlim([-8, 8])
ax.set_ylim([-8, 8])
ax.set_zlim([-8, 8])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

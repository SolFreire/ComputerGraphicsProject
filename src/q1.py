import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from cube import *
from torus import *
from pipe import *

def config_ax(ax):
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([-4, 4])

def plot_faces(ax, vertices, faces, color):
    poly3d = []
    for face in faces:
        poly3d.append([vertices[i] for i in face])

    mesh = Poly3DCollection(poly3d, facecolors=color, edgecolors="black", alpha=1)

    ax.add_collection3d(mesh)

fig = plt.figure()

cube_vertices, _, cube_faces = create_cube(4)
torus_vertices, _, torus_faces = create_torus(1, 2)
control_points = [
    (0, 0, -2),
    (0, -2, 2),
    (4, 16, 8),
    (4, 16, 8)
]
pipe_vertices, _, pipe_faces = create_pipe(control_points)

ax1 = fig.add_subplot(231, projection='3d')
config_ax(ax1)
plot_faces(ax1, cube_vertices, cube_faces, "cyan")

ax4 = fig.add_subplot(234, projection='3d')
config_ax(ax4)
plot_cube(ax4, cube_vertices)

ax2 = fig.add_subplot(232, projection='3d')
config_ax(ax2)
plot_faces(ax2, torus_vertices, torus_faces, "yellow")

ax5 = fig.add_subplot(235, projection='3d')
config_ax(ax5)
plot_torus(ax5, torus_vertices)

ax3 = fig.add_subplot(233, projection='3d')
config_ax(ax3)
plot_faces(ax3, pipe_vertices, pipe_faces, "magenta")

ax6 = fig.add_subplot(236, projection='3d')
config_ax(ax6)
plot_pipe(ax6, pipe_vertices)

plt.show()

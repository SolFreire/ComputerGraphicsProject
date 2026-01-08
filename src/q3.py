import matplotlib.pyplot as plt

from cube import *
from torus import *
from pipe import *
from common import *

def plot_camera(ax, z_near=0.1, z_far=1.0, near_size=0.05, far_size=0.4, color="red", alpha=0.25):
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
    ax.scatter(0, 0, 0, s=20, color="black", depthshade=True)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube_vertices, _, _, torus_vertices, _, _, pipe_vertices, _, _ = get_polys()

RT = perspective_matrix()

cube_vertices = transform(cube_vertices, RT)
torus_vertices = transform(torus_vertices, RT)
pipe_vertices = transform(pipe_vertices, RT)

plot_cube(ax, cube_vertices)
plot_torus(ax, torus_vertices)
plot_pipe(ax, pipe_vertices)
plot_camera(ax)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

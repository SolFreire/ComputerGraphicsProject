import matplotlib.pyplot as plt

from cube import *
from torus import *
from pipe import *
from common import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube_vertices, _, _, torus_vertices, _, _, pipe_vertices, _, _ = get_polys()

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

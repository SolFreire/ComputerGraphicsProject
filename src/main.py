import matplotlib.pyplot as plt
from models.cube import create_cube
from models.torus import create_torus
from models.pipe import create_pipe

# Cria figura e eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vC, eC = create_cube(1)
xC = [v[0] for v in vC]
yC = [v[1] for v in vC]
fC = [v[2] for v in vC]
ax.scatter(xC, yC, fC, s=10)

vT, eT = create_torus(1, 3)
xT = [v[0] for v in vT]
yT = [v[1] for v in vT]
fT = [v[2] for v in vT]
ax.scatter(xT, yT, fT, s=10)


control_points = [
    (0, 0, -3),
    (1, 2, 1),
    (-1, -2, -1),
    (0, 0, 3)
]

vertices, edges = create_pipe(control_points)

xs = [v[0] for v in vertices]
ys = [v[1] for v in vertices]
zs = [v[2] for v in vertices]
ax.scatter(xs, ys, zs, s=10)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

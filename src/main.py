import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from models.cube import create_cube
from models.torus import create_torus

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

print(eT)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

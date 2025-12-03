
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#Generate a triangular mesh from a 3D scalar field using the Marching Cubes algorithm. Neds a implicit Surface and its respective args
def mesh_from_implicit(func, *args, **kwargs):
   
    F = func(*args, **kwargs)
    verts, faces = mesh_from_scalar_field(F)
    return verts, faces

#Plots the mesh surface 
def plot_mesh(verts, faces, color="cyan"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    mesh = Poly3DCollection(verts[faces], alpha=0.7)
    mesh.set_facecolor(color)
    ax.add_collection3d(mesh)

    ax.auto_scale_xyz(verts[:,0], verts[:,1], verts[:,2])
    plt.show()

from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def mesh_from_scalar_field(F, level=0):
    verts, faces, normals, values = measure.marching_cubes(F, level=level)
    verts = np.array(verts)
    faces = np.array(faces)
    return verts, faces

#Generate a triangular mesh from a 3D scalar field using the Marching Cubes algorithm. Neds a implicit Surface and its respective args
def mesh_from_implicit(func, *args, **kwargs):
   
    F = func(*args, **kwargs)
    verts, faces = mesh_from_scalar_field(F)
    return verts, faces

#Plots the mesh surface 
def plot_mesh(verts, faces, color="cyan"):
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection='3d')

    triangles = verts[faces]

    mesh = Poly3DCollection(triangles, alpha=0.7)
    mesh.set_edgecolor("k")
    mesh.set_facecolor(color)
    ax.add_collection3d(mesh)

    
    ax.auto_scale_xyz(verts[:,0], verts[:,1], verts[:,2])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.tight_layout()
    plt.show()
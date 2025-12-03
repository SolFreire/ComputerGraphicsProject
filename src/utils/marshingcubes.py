
#Generate a triangular mesh from a 3D scalar field using the Marching Cubes algorithm. Neds a implicit Surface
def mesh_from_scalar_field(F, level=0):
    verts, faces, normals, values = measure.marching_cubes(F, level=level)
    return verts, faces

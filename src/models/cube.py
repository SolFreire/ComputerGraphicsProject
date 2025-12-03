from defining_domain import auto_domain
# Generates a cube from its edge length. An optional origin parameter sets its position.

def create_cube(side_length, origin=(0, 0, 0)):
    if side_length <= 0:
        raise ValueError("side_length must be a positive number.")

    ox, oy, oz = origin
    half = side_length / 2
    

    vertices = [
        (ox - half, oy - half, oz - half),
        (ox + half, oy - half, oz - half),
        (ox + half, oy + half, oz - half),
        (ox - half, oy + half, oz - half),
        (ox - half, oy - half, oz + half),
        (ox + half, oy - half, oz + half),
        (ox + half, oy + half, oz + half),
        (ox - half, oy + half, oz + half),
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    return vertices, edges

def implicit_cube( side, N=80):
    
    a = side / 2.0
    X, Y, Z = auto_domain(a, N=N)
    
    F = np.maximum.reduce([np.abs(X), np.abs(Y), np.abs(Z)]) - a
    return F



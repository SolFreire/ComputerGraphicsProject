import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERMITE_MATRIX = np.array([
    [ 2, -2,  1,  1],
    [-3,  3, -2, -1],
    [ 0,  0,  1,  0],
    [ 1,  0,  0,  0],
])

def hermite_coefficients(P1, P2, T1, T2):
    G = np.vstack([P1, P2, T1, T2])
    HG = HERMITE_MATRIX @ G
    a, b, c, d = HG
    return a, b, c, d

def hermite_cubic(t, HG):
    a, b, c, d = HG
    return a*t**3 + b*t**2 + c*t + d

def hermite_cubic_derivative(t, HG):
    a, b, c, _ = HG
    return 3*a*t**2 + 2*b*t + c

def create_pipe(control_points, radius=0.3, curve_resolution=20, circle_resolution=8):
    P1, P2, T1, T2 = map(np.array, control_points)
    coeffs = hermite_coefficients(P1, P2, T1, T2)

    t_values = np.linspace(0, 1, curve_resolution)
    curve_points = np.array([
        hermite_cubic(t, coeffs) for t in t_values
    ])

    tangents = np.array([
        hermite_cubic_derivative(t, coeffs) for t in t_values
    ])
    tangents = np.array([v / np.linalg.norm(v) for v in tangents])

    T0 = tangents[0]
    arbitrary = np.array([0, 0, 1])
    if abs(np.dot(T0, arbitrary)) > 0.9:
        arbitrary = np.array([1, 0, 0])

    N0 = np.cross(T0, arbitrary)
    N0 /= np.linalg.norm(N0)
    B0 = np.cross(T0, N0)

    frames = [(T0, N0, B0)]

    for i in range(1, curve_resolution):
        _, N_prev, _ = frames[-1]
        T = tangents[i]

        v = N_prev - np.dot(N_prev, T) * T
        if np.linalg.norm(v) < 1e-6:
            N = N_prev
        else:
            N = v / np.linalg.norm(v)

        B = np.cross(T, N)
        frames.append((T, N, B))

    vertices = []
    for i in range(curve_resolution):
        T, N, B = frames[i]
        center = curve_points[i]

        for a in np.linspace(0, 2*np.pi, circle_resolution, endpoint=False):
            x = center + radius * (np.cos(a)*N + np.sin(a)*B)
            vertices.append(tuple(x))

    edges = []
    for i in range(curve_resolution):
        for j in range(circle_resolution):
            a = i * circle_resolution + j
            b = i * circle_resolution + (j + 1) % circle_resolution
            edges.append((a, b))

            if i < curve_resolution - 1:
                c = (i + 1) * circle_resolution + j
                edges.append((a, c))

    return vertices, edges

def plot_pipe(ax, vertices, curve_resolution=20, circle_resolution=8):
    v = np.array(vertices)
    triangles = []

    for i in range(curve_resolution - 1):
        for j in range(circle_resolution):
            a = i * circle_resolution + j
            b = i * circle_resolution + (j + 1) % circle_resolution
            c = (i + 1) * circle_resolution + (j + 1) % circle_resolution
            d = (i + 1) * circle_resolution + j

            triangles.append([v[a], v[b], v[c]])
            triangles.append([v[a], v[c], v[d]])

    mesh = Poly3DCollection(triangles, facecolor="magenta", edgecolor="black", alpha=1)
    ax.add_collection3d(mesh)

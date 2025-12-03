import numpy as np

def bezier_cubic(t, P0, P1, P2, P3):
    return ((1 - t)**3) * P0 + \
           (3 * t * (1 - t)**2) * P1 + \
           (3 * t**2 * (1 - t)) * P2 + \
           (t**3) * P3

def bezier_cubic_derivative(t, P0, P1, P2, P3):
    return -3*(1-t)**2 * P0 + \
           (3*(1-t)**2 - 6*(1-t)*t) * P1 + \
           (6*(1-t)*t - 3*t**2) * P2 + \
           (3*t**2) * P3

def create_pipe(control_points, radius=0.3, curve_resolution=30, circle_resolution=16):
    P0, P1, P2, P3 = map(np.array, control_points)
    t_values = np.linspace(0, 1, curve_resolution)

    curve_points = np.array([bezier_cubic(t, P0, P1, P2, P3) for t in t_values])
    tangents = np.array([bezier_cubic_derivative(t, P0, P1, P2, P3) for t in t_values])
    tangents = np.array([v / np.linalg.norm(v) for v in tangents])

    up = np.array([0, 0, 1])
    vertices = []

    for i in range(curve_resolution):
        T = tangents[i]

        if abs(np.dot(T, up)) > 0.9:
            up = np.array([1, 0, 0])

        N = np.cross(T, up)
        N = N / np.linalg.norm(N)
        B = np.cross(T, N)

        for a in np.linspace(0, 2*np.pi, circle_resolution, endpoint=False):
            x = curve_points[i] + radius * (np.cos(a)*N + np.sin(a)*B)
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

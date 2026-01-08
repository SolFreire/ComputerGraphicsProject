from PIL import Image

from common import *
from q4 import *

def ndc_to_pixel(x, y, W, H):
    px = int((x + 1) * 0.5 * (W - 1))
    py = int((1 - (y + 1) * 0.5) * (H - 1))
    return px, py

def edge_intersect(y, v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    if y1 == y2:
        return None  

    if y < min(y1, y2) or y >= max(y1, y2):
        return None

    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)

def draw_edges(img, vertices, edges, edge_color):
    W, H = img.size
    pixels = img.load()

    verts = [ndc_to_pixel(x, y, W, H) for x, y in vertices]

    for a, b in edges:
        x0, y0 = verts[a]
        x1, y1 = verts[b]

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            if 0 <= x0 < W and 0 <= y0 < H:
                pixels[x0, y0] = edge_color
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy


def rasterize_polygon_scanline(img, vertices, fill_color):
    W, H = img.size
    pixels = img.load()

    verts = [ndc_to_pixel(x, y, W, H) for x, y in vertices]
    ys = [v[1] for v in verts]

    y_min = max(min(ys), 0)
    y_max = min(max(ys), H - 1)

    for y in range(y_min, y_max + 1):
        intersections = []

        for i in range(len(verts)):
            v1 = verts[i]
            v2 = verts[(i + 1) % len(verts)]

            x = edge_intersect(y, v1, v2)
            if x is not None:
                intersections.append(x)

        intersections.sort()

        
        for i in range(0, len(intersections), 2):
            if i + 1 >= len(intersections):
                break

            x_start = int(max(intersections[i], 0))
            x_end   = int(min(intersections[i + 1], W - 1))

            for x in range(x_start, x_end + 1):
                pixels[x, y] = fill_color

def raster_scene(resolution):
    W = H = resolution
    img = Image.new("RGB", (W, H), "white")

    cube_v, cube_e, cube_f, torus_v, torus_e, torus_f, pipe_v, pipe_e, pipe_f = get_polys()
    RT = perspective_matrix()

    cube_v  = transform(cube_v, RT)
    torus_v = transform(torus_v, RT)
    pipe_v  = transform(pipe_v, RT)

    cube_2d  = project_vertices(cube_v)
    torus_2d = project_vertices(torus_v)
    pipe_2d  = project_vertices(pipe_v)

    
    for face in cube_f:
        rasterize_polygon_scanline(img, [cube_2d[i] for i in face], (0, 255, 255))
    for face in torus_f:
        rasterize_polygon_scanline(img, [torus_2d[i] for i in face], (255, 255, 0))
    for face in pipe_f:
        rasterize_polygon_scanline(img, [pipe_2d[i] for i in face], (255, 0, 255))

    
    draw_edges(img, cube_2d, cube_e, (0, 120, 120))
    draw_edges(img, torus_2d, torus_e, (120, 120, 0))
    draw_edges(img, pipe_2d, pipe_e, (120, 0, 120))

    return img

def plot_three_resolutions():
    resolutions = [32, 256, 512]
    images = []

    for res in resolutions:
        img = raster_scene(res)
        images.append(img)

    
    max_size = 512
    resized = [img.resize((max_size, max_size), Image.NEAREST) for img in images]

    
    final_img = Image.new(
        "RGB",
        (max_size * 3, max_size),
        "white"
    )

    for i, img in enumerate(resized):
        final_img.paste(img, (i * max_size, 0))

    final_img.show()
    final_img.save("raster_comparacao_resolucoes.png")
    
plot_three_resolutions()
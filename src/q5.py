from PIL import Image
import math
from common import *
from q4 import *

def ndc_to_pixel(x, y, W, H):
    px = int((x + 1) * 0.5 * (W - 1))
    py = int((1 - (y + 1) * 0.5) * (H - 1))
    return px, py

def draw_pixel(img, zbuffer, x, y, z, color):
    W, H = img.size
    if 0 <= x < W and 0 <= y < H:
        if z < zbuffer[y][x]:
            zbuffer[y][x] = z
            img.putpixel((x, y), color)

def edge_intersect(y, v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    if y1 == y2:
        return None
    if y < min(y1, y2) or y >= max(y1, y2):
        return None
    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)

def rasterize_polygon_scanline(img, zbuffer, verts_2d, verts_3d, color):
    W, H = img.size
    verts_px = [ndc_to_pixel(x, y, W, H) for x, y in verts_2d]
    ys = [v[1] for v in verts_px]
    y_min = max(min(ys), 0)
    y_max = min(max(ys), H - 1)

    for y in range(y_min, y_max + 1):
        inter = []
        for i in range(len(verts_px)):
            v1 = verts_px[i]
            v2 = verts_px[(i + 1) % len(verts_px)]
            x = edge_intersect(y, v1, v2)
            if x is not None:
                z1 = verts_3d[i][2]
                z2 = verts_3d[(i + 1) % len(verts_px)][2]
                t = (y - v1[1]) / (v2[1] - v1[1])
                z = z1 + t * (z2 - z1)
                inter.append((x, z))

        inter.sort(key=lambda p: p[0])

        for i in range(0, len(inter), 2):
            if i + 1 >= len(inter):
                break
            x_start = int(max(inter[i][0], 0))
            x_end = int(min(inter[i + 1][0], W - 1))
            z_start = inter[i][1]
            z_end = inter[i + 1][1]

            for x in range(x_start, x_end + 1):
                if x_end != x_start:
                    t = (x - x_start) / (x_end - x_start)
                else:
                    t = 0
                z = z_start + t * (z_end - z_start)
                draw_pixel(img, zbuffer, x, y, z, color)

def draw_edges(img, zbuffer, verts_2d, verts_3d, edges, color):
    W, H = img.size
    verts_px = [ndc_to_pixel(x, y, W, H) for x, y in verts_2d]
    z_bias = 1e-1

    for a, b in edges:
        x0, y0 = verts_px[a]
        x1, y1 = verts_px[b]
        z0 = verts_3d[a][2]
        z1 = verts_3d[b][2]

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        steps = max(dx, dy)
        step = 0

        while True:
            if steps > 0:
                t = step / steps
            else:
                t = 0
            z = z0 + t * (z1 - z0)

            draw_pixel(img, zbuffer, x0, y0, z - z_bias, color)

            if x0 == x1 and y0 == y1:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

            step += 1

def raster_scene(res):
    W = H = res
    img = Image.new("RGB", (W, H), "white")
    zbuffer = [[float("inf")] * W for _ in range(H)]

    cube_v, cube_e, cube_f, torus_v, torus_e, torus_f, pipe_v, pipe_e, pipe_f = get_polys()
    RT = perspective_matrix()

    cube_v = transform(cube_v, RT)
    torus_v = transform(torus_v, RT)
    pipe_v = transform(pipe_v, RT)

    cube_2d = project_vertices(cube_v)
    torus_2d = project_vertices(torus_v)
    pipe_2d = project_vertices(pipe_v)

    for face in cube_f:
        rasterize_polygon_scanline(
            img, zbuffer,
            [cube_2d[i] for i in face],
            [cube_v[i] for i in face],
            (0, 255, 255)
        )

    for face in torus_f:
        rasterize_polygon_scanline(
            img, zbuffer,
            [torus_2d[i] for i in face],
            [torus_v[i] for i in face],
            (255, 255, 0)
        )

    for face in pipe_f:
        rasterize_polygon_scanline(
            img, zbuffer,
            [pipe_2d[i] for i in face],
            [pipe_v[i] for i in face],
            (255, 0, 255)
        )

    draw_edges(img, zbuffer, cube_2d, cube_v, cube_e, (0, 120, 120))
    draw_edges(img, zbuffer, torus_2d, torus_v, torus_e, (120, 120, 0))
    draw_edges(img, zbuffer, pipe_2d, pipe_v, pipe_e, (120, 0, 120))

    return img

def plot_three_resolutions():
    sizes = [32, 256, 512]
    images = [raster_scene(s) for s in sizes]
    resized = [img.resize((512, 512), Image.NEAREST) for img in images]

    final = Image.new("RGB", (1536, 512), "white")
    for i, img in enumerate(resized):
        final.paste(img, (i * 512, 0))

    final.show()
    final.save("comparacao_resolucoes.png")

plot_three_resolutions()

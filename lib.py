import numpy as np


def lerp(a, b, t):
    return (1 - t) * a + t * b


def curve(t_points, control_points):
    c = np.array([[0.0] * len(control_points[0])])

    for i in t_points:
        p0 = control_points

        while len(p0) > 1:
            p1 = []
            for j in range(len(p0) - 1):
                p1 += [lerp(p0[j], p0[j + 1], i)]
            p0 = p1

        c = np.append(c, [p0[0]], axis=0)

    c = np.delete(c, 0, axis=0)
    return c

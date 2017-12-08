import numpy as np
import math


def mandelbrot_set(height, weight, x_min, x_max, y_min, y_max, max_iter, border, f):
    array_of_colors = np.zeros((height, weight))
    for i, x in enumerate(np.arange(x_min, x_max, (x_max - x_min) / height)):
        for j, y in enumerate(np.arange(y_min, y_max, (y_max - y_min) / weight)):
            c = x + 1j * y
            z = 0
            for counter in range(max_iter):
                z = f(z) + c
                if abs(z) > border:
                    array_of_colors[i, j] = 1 / math.sqrt(counter/4 + 1)
                    break
    return -array_of_colors.T


def julia_set(height, weight, x_0, y_0, x_min, x_max, y_min, y_max, max_iter, f):
    array_of_colors = np.zeros((height, weight))
    c = x_0 + 1j * y_0
    for i, x in enumerate(np.arange(x_min, x_max, (x_max - x_min) / height)):
        for j, y in enumerate(np.arange(y_min, y_max, (y_max - y_min) / weight)):
            z = x - 1j*y
            for color_value in range(max_iter):
                z = f(z) + c
                if abs(z) > (1 + math.sqrt(1 + 4 * abs(c))) / 2:
                    array_of_colors[i, j] = 1 / math.sqrt(color_value/4 + 1)
                    break
    return -array_of_colors.T

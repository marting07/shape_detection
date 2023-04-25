import numpy as np
import math


def hough_transform_circle(points, radius_range, accumulator_threshold):
    max_x, max_y = np.max(points, axis=0)
    min_x, min_y = np.min(points, axis=0)
    accumulator = np.zeros((max_x + 1, max_y + 1, radius_range[1] - radius_range[0] + 1), dtype=int)
    for point in points:
        x, y = point
        for radius in range(radius_range[0], radius_range[1] + 1):
            for theta in range(360):
                theta_rad = math.radians(theta)
                x_c = int(round(x - radius * math.cos(theta_rad)))
                y_c = int(round(y - radius * math.sin(theta_rad)))

                if 0 <= x_c < max_x + 1 and 0 <= y_c < max_y + 1:
                    accumulator[x_c, y_c, radius - radius_range[0]] += 1
    circles = []
    for x_c, y_c, radius in zip(*np.where(accumulator > accumulator_threshold)):
        circles.append((x_c, y_c, radius + radius_range[0]))
    return circles

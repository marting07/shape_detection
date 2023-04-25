import numpy as np
import math


def hough_transform_line(points, num_angle_bins, rho_max, threshold):
    accumulator = np.zeros((2 * rho_max, num_angle_bins), dtype=int)
    for point in points:
        x, y = point
        for theta_idx in range(num_angle_bins):
            theta = math.pi * theta_idx / num_angle_bins
            rho = int(round(x * math.cos(theta) + y * math.sin(theta)) + rho_max)
            accumulator[rho, theta_idx] += 1
    lines = []
    for rho_idx, theta_idx in zip(*np.where(accumulator > threshold)):
        rho = rho_idx - rho_max
        theta = math.pi * theta_idx / num_angle_bins
        lines.append((rho, theta))
    return lines

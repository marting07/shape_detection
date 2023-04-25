import random
import math

def line_from_points(p1, p2):
    a = (p1[1] - p2[1])
    b = (p2[0] - p1[0])
    c = (p1[0] * p2[1] - p2[0] * p1[1])
    return a, b, -c

def distance_point_to_line(a, b, c, point):
    x, y = point
    return abs(a * x + b * y + c) / math.sqrt(a * a + b * b)

def ransac_line(points, num_iterations, threshold):
    best_model = None
    best_inliers = []
    for _ in range(num_iterations):
        # Randomly select 2 points
        p1, p2 = random.sample(points, 2)
        # Calculate line coefficients
        a, b, c = line_from_points(p1, p2)
        # Find inliers
        inliers = [point for point in points if distance_point_to_line(a, b, c, point) < threshold]
        # Update best model
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_model = (a, b, c)
    return best_model, best_inliers

import random
import math

def circle_from_points(p1, p2, p3):
    A = p2[0] - p1[0]
    B = p2[1] - p1[1]
    C = p3[0] - p1[0]
    D = p3[1] - p1[1]
    E = A * (p1[0] + p2[0]) + B * (p1[1] + p2[1])
    F = C * (p1[0] + p3[0]) + D * (p1[1] + p3[1])
    G = 2 * (A * (p3[1] - p2[1]) - B * (p3[0] - p2[0]))
    if G == 0:
        return None
    center_x = (D * E - B * F) / G
    center_y = (A * F - C * E) / G
    radius = math.sqrt((p1[0] - center_x)**2 + (p1[1] - center_y)**2)
    return center_x, center_y, radius

def distance_point_to_circle(center, radius, point):
    x, y = point
    center_x, center_y = center
    return abs(math.sqrt((x - center_x)**2 + (y - center_y)**2) - radius)

def ransac_circle(points, num_iterations, threshold):
    best_model = None
    best_inliers = []
    for _ in range(num_iterations):
        # Randomly select 3 non-collinear points
        p1, p2, p3 = random.sample(points, 3)
        circle_params = circle_from_points(p1, p2, p3)
        # If the points are collinear, circle_params will be None
        if not circle_params:
            continue
        center, radius = circle_params[:-1], circle_params[-1]
        # Find inliers
        inliers = [point for point in points if distance_point_to_circle(center, radius, point) < threshold]
        # Update best model
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_model = circle_params
    return best_model, best_inliers

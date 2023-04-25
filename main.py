# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from non_parametric.ransac_line import ransac_line
from non_parametric.ransac_circle import ransac_circle
import matplotlib.pyplot as plt
import math
from parametric.hough_circle import hough_transform_circle
from parametric.hough_line import hough_transform_line


def ransac_line_example():
    # RANSAC for lines
    points = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9), (10, 2), (11, 1), (12, 0)]
    num_iterations = 1000
    threshold = 1.0
    best_model, best_inliers = ransac_line(points, num_iterations, threshold)
    print("Best model (a, b, c):", best_model)
    print("Best inliers:", best_inliers)
    # Plot
    # Draw points
    px, py = zip(*points)
    plt.scatter(px, py, c="red", label="Data points")
    # Draw best-fitting line
    a, b, c = best_model
    x = range(int(min(px)) - 1, int(max(px)) + 2)
    y = [(-a * xi - c) / b for xi in x]
    plt.plot(x, y, c="blue", label="Best-fitting line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("RANSAC Line Fitting")
    plt.legend()
    plt.grid(True)
    plt.show()


def ransac_circle_example():
    # RANSAC for circles
    points = [(2, 2), (4, 2), (3, 4), (2, 6), (4, 6), (8, 8), (10, 10), (12, 12)]
    num_iterations = 1000
    threshold = 1.0
    best_model, best_inliers = ransac_circle(points, num_iterations, threshold)
    print("Best model (center_x, center_y, radius):", best_model)
    print("Best inliers:", best_inliers)
    # Plot
    # Draw points
    px, py = zip(*points)
    plt.scatter(px, py, c="red", label="Data points")
    # Draw best-fitting circle
    center_x, center_y, radius = best_model
    circle = plt.Circle((center_x, center_y), radius, color="blue", fill=False, label="Best-fitting circle")
    ax = plt.gca()
    ax.add_artist(circle)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("RANSAC Circle Fitting")
    plt.legend([circle], ['Best-fitting circle'])
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def hough_transform_line_example():
    points = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9), (10, 2), (11, 1), (12, 0)]
    num_angle_bins = 360
    rho_max = 20
    threshold = 4
    lines = hough_transform_line(points, num_angle_bins, rho_max, threshold)
    # Draw points
    px, py = zip(*points)
    plt.scatter(px, py, c="red", label="Data points")
    # Draw detected lines
    x = range(int(min(px))-1, int(max(px))+2)
    for rho, theta in lines:
        if theta == 0:
            plt.axvline(x=rho, color="blue")
        else:
            a = -math.cos(theta) / math.sin(theta)
            b = rho / math.sin(theta)
            y = [a*xi + b for xi in x]
            plt.plot(x, y, c="blue")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Hough Transform Line Detection")
    plt.legend()
    plt.grid(True)
    plt.show()


def hough_transform_circle_example():
    points = [(2, 2), (4, 2), (3, 4), (2, 6), (4, 6), (8, 8), (10, 10), (12, 12)]
    radius_range = (2, 5)
    accumulator_threshold = 4
    circles = hough_transform_circle(points, radius_range, accumulator_threshold)
    # Draw points
    px, py = zip(*points)
    plt.scatter(px, py, c="red", label="Data points")
    # Draw detected circles
    ax = plt.gca()
    for x_c, y_c, radius in circles:
        circle = plt.Circle((x_c, y_c), radius, color="blue", fill=False)
        ax.add_artist(circle)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Hough Transform Circle Detection")
    plt.legend([circle], ['Detected circles'])
    plt.axis("equal")
    plt.grid(True)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ransac_line_example()
    ransac_circle_example()
    hough_transform_line_example()
    hough_transform_circle_example()

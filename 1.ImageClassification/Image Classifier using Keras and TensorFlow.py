import matplotlib.pyplot as plt

def plot_circle_points(x, y):
    points = [
        (x, y), (y, x), (-x, y), (-y, x),
        (-x, -y), (-y, -x), (x, -y), (y, -x)
    ]
    return points

def midpoint_circle(radius):
    x = 0
    y = radius
    p = 1 - radius
    all_points = []

    while x <= y:
        all_points += plot_circle_points(x, y)
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x + 1 - 2 * y

    return all_points

# Plotting
points = midpoint_circle(7)
x_vals, y_vals = zip(*points)

plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='blue')
plt.title("Midpoint Circle (Radius 7)")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()

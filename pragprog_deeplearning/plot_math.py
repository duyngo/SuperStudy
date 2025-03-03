# Plot the reservations/pizzas dataset.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def show_plot_01():
    plt.axis([0, 50, 0, 50])                                 # scale axes (0 to 50)
    plt.xticks(fontsize=15)                                  # set x axis ticks
    plt.yticks(fontsize=15)                                  # set y axis ticks
    plt.xlabel("Reservations", fontsize=30)                  # set x axis label
    plt.ylabel("Pizzas", fontsize=30)                        # set y axis label
    path = "/Users/duyngoft/F4UPW/SuperStudy/pragprog_deeplearning/02_first/pizza.txt"
    X, Y = np.loadtxt(path, skiprows=1, unpack=True)  # load data
    plt.plot(X, Y, "bo")                                     # plot data
    plt.show()                                               # display chart
    return True                                                                                 

def show_plot_02():
    #Add linear regression line y = 2x + 1
    x = np.linspace(0, 50, 100)
    y = 2 * x + 50
    plt.plot(x, y, "r-", label="y = 2x + 50")                 # plot regression line
    plt.legend(fontsize=15)                                  # add legend
    plt.show()
    return True


def show_plot_03():
    x_edge, y_edge = 50, 50
    plt.axis([0, x_edge, 0, y_edge])
    plt.plot([0, x_edge], [0, y_edge], linewidth=1.0, color="r")
    plt.show()
    return True


def show_plot_04():
    # Define the range for W and b
    W_values = np.linspace(0, 100, 50)  # 50 steps from 0 to 100
    b_values = np.linspace(0, 100, 50)  # 50 steps from 0 to 100

    # Create x values
    x = np.linspace(-10, 10, 100)

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1050)  # Adjusted for large b values
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Dynamic Changes in y = Wx + b")

    # Line plot
    line, = ax.plot([], [], 'r-', linewidth=2)

    # Update function for animation
    def update(frame):
        W = W_values[frame]
        b = b_values[frame]
        y = W * x + b  # Compute y values
        line.set_data(x, y)
        ax.set_title(f"y = {W:.2f}x + {b:.2f}")
        return line,

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=len(W_values), interval=200, blit=True)

    # Save animation as a GIF
    gif_path = "/Users/duyngoft/Downloads/linear_regression_dynamic.gif"
    ani.save(gif_path, writer='pillow')

    # Return the GIF path
    return gif_path

# show_plot_01()
# show_plot_02()
# show_plot_03()
show_plot_04()
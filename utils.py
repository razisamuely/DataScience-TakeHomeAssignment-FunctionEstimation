import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme()
from IPython.display import clear_output
import pandas as pd


def check_if_below(x: float, y: float, func):
    """
    This function checks if the output of the function func(x) is below a given value y.

    Parameters:
    x (float): the input value for the function func(x)
    y (float): the value to compare the output of func(x) against
    func (function): a function that takes one float argument and returns a float
                     e.g. def func(x): return x**2

    Returns:
    bool: True if the output of func(x) is greater than y, otherwise False
    """
    y_output = func(x=x)
    return y_output > y


def find_y_value(x: float, func, epsilon: float, lower_bound: float = 0, upper_bound: float = 1):
    """
    This function uses binary search to find the value of y such that the
    function func(x,y) returns a value close to x within the given epsilon.

    Parameters:
    x (float): the value that the function func(x,y) is trying to approximate
    func (function): a function that takes two float arguments and returns a float
                     e.g. def func(x, y): return x + y
    epsilon (float): the maximum difference between the output of func(x,y) and x
                     that is considered acceptable
    lower_bound (float): the lower bound of the search range for y (default: 0)
    upper_bound (float): the upper bound of the search range for y (default: 1)

    Returns:
    float: the value of y that, when passed to func(x,y), produces a value close to x within epsilon
    """

    while True:
        mid_point = (lower_bound + upper_bound) / 2

        if check_if_below(x, mid_point, func=func):
            if upper_bound - mid_point < epsilon:
                return mid_point
            lower_bound = mid_point
        else:
            if mid_point - lower_bound < epsilon:
                return mid_point
            upper_bound = mid_point


def find_y_value_with_plot(x: float, func, epsilon: float, lower_bound: float = 0, upper_bound: float = 1):
    """
    This function uses binary search to find the value of y such that the
    function func(x,y) returns a value close to x within the given epsilon.
    It also plots the progress of the search to help visualize the algorithm.

    Parameters:
    x (float): the value that the function func(x,y) is trying to approximate
    func (function): a function that takes two float arguments and returns a float
                     e.g. def func(x, y): return x + y
    epsilon (float): the maximum difference between the output of func(x,y) and x
                     that is considered acceptable
    lower_bound (float): the lower bound of the search range for y (default: 0)
    upper_bound (float): the upper bound of the search range for y (default: 1)

    Returns:
    float: the value of y that, when passed to func(x,y), produces a value close to x within epsilon
    """
    x_space = np.arange(lower_bound, upper_bound, epsilon)
    y_space = np.arange(lower_bound, upper_bound, epsilon)

    y = func(x=x)

    while True:

        mid_point = (lower_bound + upper_bound) / 2

        # plot the current state of the search
        plt.scatter(x, y, c='green')
        graph = sns.lineplot(x=x_space, y=y_space)
        graph.axhline(mid_point, c='orange', xmin=x - 0.1, xmax=x + 0.2)
        plt.show()
        clear_output(wait=True)

        # check if the current mid-point is the desired value
        if check_if_below(x, mid_point, func=func):
            if upper_bound - mid_point < epsilon:
                return mid_point
            lower_bound = mid_point
        else:
            if mid_point - lower_bound < epsilon:
                return mid_point
            upper_bound = mid_point


def create_gif_of_MonteCarlo_simulation(start, end, func, samples=[50, 100, 300, 700, 800, 900]):

    """
    This function creates a Monte Carlo simulation of a function and saves a GIF
    of the simulation's progress over time. It generates random samples of the
    function and plots them to show how well the simulation is converging to the
    true value of the function.

    Parameters:
    start (float): the start of the interval for x values
    end (float): the end of the interval for x values
    func (function): a function that takes a float argument and returns a float
                     e.g. def func(x): return x**2
    samples (list): a list of integers that specify the number of samples to generate
                     at each step of the simulation (default: [50, 100, 300, 700, 800, 900])

    """

    # Creating data
    x_space = np.arange(start, end, 0.01)
    y_space = [func(i) for i in x_space]

    for k in samples:
        uniform_sample = [np.random.uniform(0, 1, 2) for i in range(k)]

        # Ploting f(x) = x line
        sns.lineplot(x=x_space, y=y_space)

        # Plot below and bove points
        points = uniform_sample
        c = 0
        for x, y in points:
            color = 'blue' if check_if_below(x=x, y=y, func=func) else 'red'
            c += color == 'blue'
            plt.scatter(x, y, c=color)

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.title(f"{k} Sampels , proportion = {c / k:.2}")

        plt.show()
        clear_output(wait=True)


def plot_example_of_different_functions():
    for j in np.arange(0.1, 6, 0.03):
        # Defininf function f(x) = x
        def example_function(x: float):
            return x ** j

        # Creating data
        x = np.arange(0, 1, 0.01)
        y = [example_function(x=i) for i in x]
        df = pd.DataFrame({"x": x, "y": y})

        # Ploting f(x) = x line
        sns.lineplot(data=df, x="x", y="y")

        # Plot below and bove points
        points = [(0.1, 0.2), (0.1, 0.8), (0.6, 0.8), (0.5, 0.5), (0.5, 0.5),
                  (0.1, 0.05), (0.1, 0.02), (0.6, 0.1), (0.9, 0.9), (0.95, 0.05)
                  ]
        for x, y in points:
            color = 'blue' if check_if_below(x=x, y=y, func=example_function) else 'red'
            plt.scatter(x, y, c=color)

        plt.xlim(0, 1)
        plt.ylim(0, 1)

        plt.show()
        clear_output(wait=True)

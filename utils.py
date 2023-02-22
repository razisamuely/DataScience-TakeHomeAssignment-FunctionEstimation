import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_theme()
from IPython.display import clear_output


def check_if_below(x: float, y: float, func):
    y_output = func(x=x)
    return y_output > y


def binary_search(low, high, x, epsilon, func):
    if high >= low:

        mid = (high + low) / 2
        if high - low < epsilon:
            return mid

        position = check_if_below(x=x, y=mid, func=func)

        if position:
            return binary_search(low=mid, high=high, x=x, epsilon=epsilon, func=func)

        else:
            return binary_search(low=low, high=mid, x=x, epsilon=epsilon, func=func)


def binary_search_with_plot(low, high, x, epsilon, func, x_space, y_space):
    mid = (high + low) / 2

    # plot
    y = func(x=x)
    plt.scatter(x, y, c='green')
    graph = sns.lineplot(x=x_space, y=y_space)
    graph.axhline(mid, c='orange', xmin=x - 0.1, xmax=x + 0.2)
    plt.show()
    clear_output(wait=True)

    if high - low < epsilon:
        return mid

    position = check_if_below(x=x, y=mid, func=func)

    if position:
        return binary_search_with_plot(low=mid, high=high, x=x, epsilon=epsilon, func=func, x_space=x_space,
                                       y_space=y_space)

    else:
        return binary_search_with_plot(low=low, high=mid, x=x, epsilon=epsilon, func=func, x_space=x_space,
                                       y_space=y_space)


def create_gif_of_MonteCarlo_simulation(start, end, func, samples = [50, 100, 300, 700, 800, 900]):
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

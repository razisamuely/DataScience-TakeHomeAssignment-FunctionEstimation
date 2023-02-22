import seaborn as sns
import matplotlib.pyplot as plt

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

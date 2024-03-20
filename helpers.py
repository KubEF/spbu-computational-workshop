from typing import Callable


def generate_xs(left_bound: float, right_bound: float, count_of_xs: int) -> list[float]:
    """
    Generate specified count of equidistant xs in specified bounds
    :param left_bound: left bound
    :param right_bound: right bound
    :param count_of_xs: count of generated xs
    :return: list of xs
    """

    step = (right_bound - left_bound) / count_of_xs
    return [left_bound + i * step for i in range(count_of_xs + 1)]


def generate_values(func: Callable[[float], float], xs: list[float]) -> list[float]:
    """
    Generate values of function by given points
    :param func: function to calculate
    :param xs: values of arguments
    :return: list of calculated values
    """
    return [func(i) for i in xs]

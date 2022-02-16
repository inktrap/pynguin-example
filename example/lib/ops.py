from typing import Union

numeric = Union[int, float, complex]


def minus(a: numeric, b: numeric) -> numeric:
    """
    :param a: the first numeric operand
    :param b: the second numeric operand
    :returns: result of substraction

    """
    return a - b


def plus(a: numeric, b: numeric) -> numeric:
    """
    :param a: the first numeric operand
    :param b: the second numeric operand
    :returns: result of addition

    """
    return a + b

#!/usr/bin/env python3.9

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


def main() -> None:
    """Main method.
    :returns: None

    """
    print(plus(1, 2))
    print(minus(1, 2))


if __name__ == "__main__":
    main()

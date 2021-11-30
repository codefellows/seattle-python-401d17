from factorial.factorial import factorial
import pytest


def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


def test_factorial_5():
    actual = factorial(5)
    expected = 120
    assert actual == expected

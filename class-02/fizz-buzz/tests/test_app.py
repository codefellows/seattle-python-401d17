from fizz_buzz_package.fizz_buzz_module import fizz_buzz
import pytest


def test_import():
    assert fizz_buzz


def test_fizz_buzz_one():
    actual = fizz_buzz(1)
    expected = "1"
    assert actual == expected


def test_fizz_buzz_two():
    actual = fizz_buzz(2)
    expected = "2"
    assert actual == expected


def test_fizz_buzz_three():
    actual = fizz_buzz(3)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_four():
    actual = fizz_buzz(4)
    expected = "4"
    assert actual == expected


def test_fizz_buzz_five():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_fizz_buzz_six():
    actual = fizz_buzz(6)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_ten():
    actual = fizz_buzz(10)
    expected = "Buzz"
    assert actual == expected


def test_fizz_buzz_fifteen():
    actual = fizz_buzz(15)
    expected = "Fizz Buzz"
    assert actual == expected


def test_fizz_buzz_thirty():
    actual = fizz_buzz(30)
    expected = "Fizz Buzz"
    assert actual == expected

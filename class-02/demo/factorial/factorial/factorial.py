def factorial(n):
    """
    return n! (as it's sometimes written)
    e.g. factorial(4) = 4 * 3 * 2 * 1 = 24
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)

    """
                factorial(1) -> base case
            factorial(2)
        factorial(3)
    factorial(4)
    """

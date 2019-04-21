"""
Implement a fibonnaci sequence in three different ways:
* recursively
* dynamically (using memoization to store results)
* interatively
"""

import unittest


def fib_rec(n: int) -> int:
    """
    Find the nth number in the fibonnaci sequency using recursion
    This method has a time complexity of O(2^n)

    Arguments:
        n {int} -- which number in sequence

    Returns:
        int -- answer
    """

    # base case
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dynam(n: int, cache) -> int:
    """
    Find the nth number in the fibonnaci sequency dynamically

    Arguments:
        n {int} -- which number in sequence

    Returns:
        int -- answer
    """

    # base case
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dynam(n - 1, cache) + fib_dynam(n - 2, cache)

    return cache[n]


def fib_iter(n: int) -> int:
    """
    Find the nth number in the fibonnaci sequency iteratively

    Arguments:
        n {int} -- which number in sequence

    Returns:
        int -- answer
    """

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


class TestFibonnaci(unittest.TestCase):

    def test_permute(self):
        self.assertEqual(fib_rec(1), 1)
        self.assertEqual(fib_rec(10), 55)
        self.assertEqual(fib_rec(23), 28657)
        cache = [None] * (23 + 1)
        self.assertEqual(fib_dynam(23, cache), 28657)
        self.assertEqual(fib_dynam(10, cache), 55)
        self.assertEqual(fib_dynam(1, cache), 1)
        self.assertEqual(fib_iter(1), 1)
        self.assertEqual(fib_iter(10), 55)
        self.assertEqual(fib_iter(23), 28657)


if __name__ == '__main__':
    unittest.main()

"""
Find all perumations of a string using recursion
Do not use itertools
"""

import unittest


def permute(s: str) -> list:
    """
    Find all permutations of a string using recursion.
    Note duplicates are allowed.

    Arguments:
        s {str} -- input string

    Returns:
        list -- list of string permutations
    """

    out = []

    # base Case
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]

    return out


class TestPermute(unittest.TestCase):

    def test_permute(self):
        self.assertEqual(sorted(permute('abc')), sorted(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(permute('dog')), sorted(
            ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))


if __name__ == '__main__':
    unittest.main()

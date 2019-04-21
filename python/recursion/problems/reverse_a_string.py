"""
Reverse a string using recursion
"""

import unittest


def reverse(s: str) -> str:
    """
    Reverse an input string via recursion

    Arguments:
        s {str} -- string to be reversed

    Returns:
        str -- reversed string
    """

    # base case
    if len(s) <= 1:
        return s

    # recursion
    return reverse(s[1:]) + s[0]


class TestReverse(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse('hello world'), 'dlrow olleh')
        self.assertEqual(reverse('123456789'), '987654321')


if __name__ == '__main__':
    unittest.main()

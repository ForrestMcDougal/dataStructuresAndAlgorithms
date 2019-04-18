"""
Given a string of opening and closing parentheses, check whether
it's balanced. You can assume the input string has no spaces.
"""

import unittest


def balance_check(s: str) -> bool:
    """
    Checks whether brackets are balanced in a given string
    Strings should only consist of brackets and have no whitespace

    Arguments:
        s {str} -- string of brackets

    Returns:
        bool -- wheter or not the string is balanced
    """

    # edge case
    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


class TestBalanceCheck(unittest.TestCase):
    def test_balance_check(self):
        self.assertTrue(balance_check('[]'))
        self.assertTrue(balance_check('()'))
        self.assertTrue(balance_check('{}'))
        self.assertFalse(balance_check('[)'))
        self.assertTrue(balance_check('[()]'))
        self.assertTrue(balance_check('[({})]'))
        self.assertTrue(balance_check('[{()}]'))
        self.assertFalse(balance_check('[(])'))
        self.assertTrue(balance_check('[](){([[[]]])}'))
        self.assertFalse(balance_check('()(){]}'))


if __name__ == '__main__':
    unittest.main()

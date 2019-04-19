"""
Given a string, determine if it is compreised of all unique characters.
'abcde' has all unique characters and should return True
'aabcde' contains duplicate characters and should return False

Solution:
use a set of the given string and compare it's length to given string
or add each letter to a set and compare if letter in in the set
"""

import unittest


def uni_char_set_len(s: str) -> bool:
    """
    Checks for duplicate characters in a given string.
    Uses sets to remove duplicates and compares length.

    Arguments:
        s {str} -- string to check

    Returns:
        bool -- whether any duplicate characters exist
    """

    return len(set(s)) == len(s)


def uni_char(s: str) -> bool:
    """
    Checks for duplicate characters in a given string.
    Checks whether each letter in string is in a set.

    Arguments:
        s {str} -- string to check

    Returns:
        bool -- whether any duplicate characters exist
    """

    # edge case
    if len(s) == 0:
        return True

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True


class TestUniChar(unittest.TestCase):
    def test_uni_char(self):
        self.assertTrue(uni_char(''))
        self.assertFalse(uni_char('goo'))
        self.assertTrue(uni_char('abcdefg'))

    def test_uni_char_set_len(self):
        self.assertTrue(uni_char_set_len(''))
        self.assertFalse(uni_char_set_len('goo'))
        self.assertTrue(uni_char_set_len('abcdefg'))


if __name__ == '__main__':
    unittest.main()

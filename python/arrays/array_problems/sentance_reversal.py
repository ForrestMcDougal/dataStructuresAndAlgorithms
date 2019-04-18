"""
Given a string of words, reverse all the words.
For example:
Given: 'This is the best'
Return: 'best the is This'

Solution:
Using pythons built in split() and slicing or reversed function.
Or implementing split() and using reversed.
"""

import unittest


def rev_word_reversed(s: str) -> str:
    """
    Reverses the words in a given string after removing whitespace.
    Uses python's reversed function

    Arguments:
        s {str} -- String to reverse order of words

    Returns:
        str -- Reverse order of string
    """

    return ' '.join(reversed(s.split()))


def rev_word_slice(s: str) -> str:
    """
    Reverses the words in a given string after removing whitespace.
    Uses python's slicing

    Arguments:
        s {str} -- String to reverse order of words

    Returns:
        str -- Reverse order of string
    """

    return ' '.join(s.split()[::-1])


def rev_word(s: str) -> str:
    """
    Reverses the words in a given string after removing whitespace.
    Uses python's reversed function after implementing the split method.

    Arguments:
        s {str} -- String to reverse order of words

    Returns:
        str -- Reverse order of string
    """

    words = []
    length = len(s)
    space = [' ']

    i = 0
    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(words))


class TestRevWord(unittest.TestCase):
    def test_rev_word(self):
        self.assertEqual(rev_word('Hi John,   are you ready to go?'),
                         'go? to ready you are John, Hi')
        self.assertEqual(rev_word('      space before'), 'before space')
        self.assertEqual(rev_word('space after     '), 'after space')
        self.assertEqual(rev_word('1'), '1')

    def test_rev_word_reversed(self):
        self.assertEqual(rev_word_reversed('Hi John,   are you ready to go?'),
                         'go? to ready you are John, Hi')
        self.assertEqual(rev_word_reversed(
            '      space before'), 'before space')
        self.assertEqual(rev_word_reversed('space after     '), 'after space')
        self.assertEqual(rev_word_reversed('1'), '1')

    def test_rev_word_slice(self):
        self.assertEqual(rev_word_slice('Hi John,   are you ready to go?'),
                         'go? to ready you are John, Hi')
        self.assertEqual(rev_word_slice('      space before'), 'before space')
        self.assertEqual(rev_word_slice('space after     '), 'after space')
        self.assertEqual(rev_word_slice('1'), '1')


if __name__ == '__main__':
    unittest.main()

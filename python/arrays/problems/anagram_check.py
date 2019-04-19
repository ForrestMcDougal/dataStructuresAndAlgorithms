"""
Given two strings, check to see if they are anagram_sorts.
An anagram_sort is when the two strings can be written using the exact
same letters.
(spaces and capitalization ignored)
"""

import unittest


def anagram_sort(s1: str, s2: str) -> bool:
    """
    Finds anagrams by comparing sorted strings

    Arguments:
        s1 {str} -- first string
        s2 {str} -- second string

    Returns:
        bool -- whether the two strings are anagrams
    """

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


def anagram(s1: str, s2: str) -> bool:
    """
    Finds anagrams by using a dictionary

    Arguments:
        s1 {str} -- first string
        s2 {str} -- second string

    Returns:
        bool -- whether the two strings are anagrams
    """

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    for k in count:
        if count[k] != 0:
            return False

    return True


class TestAnagram(unittest.TestCase):
    def test_anagram_sort(self):
        self.assertTrue(anagram_sort('dog', 'God'))
        self.assertTrue(anagram_sort('rail safety', 'fairy tales'))
        self.assertTrue(anagram_sort('eleven plus two', 'twelve plus one'))
        self.assertTrue(anagram_sort('Clint Eastwood', 'old west action'))
        self.assertTrue(anagram_sort(
            'I am Lord Voldemort', 'Tom Marvolo Riddle'))
        self.assertFalse(anagram_sort('no', 'yes'))
        self.assertFalse(anagram_sort('color', 'colour'))

    def test_anagram(self):
        self.assertTrue(anagram('dog', 'God'))
        self.assertTrue(anagram('rail safety', 'fairy tales'))
        self.assertTrue(anagram('eleven plus two', 'twelve plus one'))
        self.assertTrue(anagram('Clint Eastwood', 'old west action'))
        self.assertTrue(anagram(
            'I am Lord Voldemort', 'Tom Marvolo Riddle'))
        self.assertFalse(anagram('no', 'yes'))
        self.assertFalse(anagram('color', 'colour'))


if __name__ == '__main__':
    unittest.main()

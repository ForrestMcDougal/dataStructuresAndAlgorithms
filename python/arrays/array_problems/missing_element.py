"""
Consider an array of non-negative integers. A second array is
formed by shuffling the elements of the first array and deleting
a random element. Given these two arrays, find which element is 
missing in the second array.

Solution:
First, sort the first array. Then check whether an element in
the first array appears in the second via binary search. Duplicate
elements can be problematic. The complexity is O(NlogN).
"""

import unittest
import collections


def finder_sort(arr1: list, arr2: list) -> int:
    """
    Finds missing element using sorting

    Arguments:
        arr1 {list} -- array with missing element
        arr2 {list} -- array without missing element

    Returns:
        int -- missing element
    """

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


def finder(arr1: list, arr2: list) -> int:
    """
    Finds missing via dictionary method

    Arguments:
        arr1 {list} -- array with missing element
        arr2 {list} -- array without missing element

    Returns:
        int -- missing element
    """

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


class TestFinder(unittest.TestCase):
    def test_finder_sort(self):
        self.assertEqual(finder_sort([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(finder_sort(
            [1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(finder_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], [
                         9, 8, 7, 5, 4, 3, 2, 1]), 6)

    def test_finder(self):
        self.assertEqual(finder([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [
                         9, 8, 7, 5, 4, 3, 2, 1]), 6)


if __name__ == '__main__':
    unittest.main()

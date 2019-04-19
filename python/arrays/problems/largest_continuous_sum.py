"""
Given an array of integers (positive and negative)
find the largest continuous sum.

Solution:
If the array is all positive, simply sum up the array.
If negative numbers are present, check if current sum is larger
than maximum. If it is, update current sum.
"""

import unittest


def largest_cont_sum(arr: list) -> int:
    """
    Finds the largest continuous sum of numbers in a given array

    Arguments:
        arr {list} -- array of numbers

    Returns:
        int -- largest maximum sum
    """

    if len(arr) == 0:
        return None

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


class TestLargestContSum(unittest.TestCase):
    def test_largest_cont_sum(self):
        self.assertEqual(largest_cont_sum(
            [1, 2, -1, 3, 4, 10, 10, -10, 1]), 29)
        self.assertEqual(largest_cont_sum([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(largest_cont_sum([-1, 1]), 1)
        self.assertEqual(largest_cont_sum([]), None)


if __name__ == '__main__':
    unittest.main()

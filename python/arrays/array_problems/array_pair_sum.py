"""
Given an integer array, output all the unique pairs
that sum up to a specific value k

So the input:
pair_sum([1, 3, 2, 2], 4)

would return 2 pairs:
(1, 3)
(2, 2)

Solution:
The O(N) algorith uses the set data structure.
Perform a linear pass from the beginning and for each element
check whether k-element is in the set of seen numbers.
If it is, then find a pair of sum k and add it to the output.
If not, this element does not belong to a pair yet, so add it to the 
set of seen elements
"""

import unittest


def pair_sum_num(arr: list, k: int) -> int:
    """
    Find number of pairs

    Arguments:
        arr {list} -- array of numbers
        k {int} -- target sum

    Returns:
        int -- number of matches
    """

    if len(arr) < 2:
        return

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


def pair_sum(arr: list, k: int) -> set:
    """
    Find all pairs

    Arguments:
        arr {list} -- array of numbers
        k {int} -- target sum

    Returns:
        set -- tuples of pairs
    """

    if len(arr) < 2:
        return

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return output


class TestPairSum(unittest.TestCase):
    def test_pair_sum_num(self):
        self.assertEqual(pair_sum_num([1, 3, 2, 2], 4), 2)
        self.assertEqual(pair_sum_num(
            [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(pair_sum_num([1, 2, 3, 1], 3), 1)

    def test_pair_sum(self):
        self.assertEqual(pair_sum([1, 3, 2, 2], 4), {(1, 3), (2, 2)})
        self.assertEqual(pair_sum(
            [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), {(4, 6), (5, 5), (2, 8), (-1, 11), (1, 9), (3, 7)})
        self.assertEqual(pair_sum([1, 2, 3, 1], 3), {(1, 2)})


if __name__ == '__main__':
    unittest.main()

"""
Given a target amount n and a list of distinct coin values, what's the
fewest coins needed to make the change amount?
"""

import unittest


def change(target: int, coins: list, known_results) -> int:
    """
    Find the minimum number of coins given back

    Arguments:
        target {int} -- change due
        coins {list} -- (limitless) coin denominations
        known_rewults -- used for memoization. DO NOT PASS USER DEFINED VALUE.

    Returns:
        int -- least amount of coins given back
    """

    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + change(target - i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins

    return min_coins


class TestChange(unittest.TestCase):

    def test_change(self):
        known_results = [0] * 100
        self.assertEqual(change(45, [1, 5, 10, 25], known_results), 3)
        self.assertEqual(change(23, [1, 5, 10, 25], known_results), 5)
        self.assertEqual(change(74, [1, 5, 10, 25], known_results), 8)


if __name__ == '__main__':
    unittest.main()

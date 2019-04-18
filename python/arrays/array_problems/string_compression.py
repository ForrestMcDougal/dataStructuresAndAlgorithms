"""
Given a string in the form 'AAAABBBBCCCCDDEEE' compress it to 
become 'A4B4C4D2E3'.
"""

import unittest


def compress(s: str) -> str:
    """
    Compress a string to remove redundant continuous strings
    and just show value and then number of continuous times it appears.

    This solution compresses without checking. Known as the RunLength 
    Compression Algorithm. Time and space complexity of O(N)

    Arguments:
        s {str} -- string to compress

    Returns:
        str -- compressed string
    """

    r = ""
    l = len(s)

    # edge cases
    if l == 0:
        return ''
    if l == 1:
        return s + '1'

    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i - 1] + str(cnt)

    return r


class TestCompress(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress('AAAAABBBBCCCC'), 'A5B4C4')
        self.assertEqual(compress(''), '')
        self.assertEqual(compress('AABBCC'), 'A2B2C2')
        self.assertEqual(compress('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertEqual(compress('AAaaBBbb'), 'A2a2B2b2')
        self.assertEqual(compress('A'), 'A1')


if __name__ == '__main__':
    unittest.main()

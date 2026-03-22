# Author: Kaustav Ghosh

class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count_a = [0] * 26
        count_b = [0] * 26
        for c in a:
            count_a[ord(c) - ord('a')] += 1
        for c in b:
            count_b[ord(c) - ord('a')] += 1
        la, lb = len(a), len(b)
        res = la + lb
        # Condition 3: make all chars in a and b the same
        for i in range(26):
            res = min(res, la + lb - count_a[i] - count_b[i])
        # Condition 1 & 2: every char in a < every char in b (or vice versa)
        # Try each boundary between char i-1 and char i
        prefix_a = 0
        prefix_b = 0
        for i in range(1, 26):
            prefix_a += count_a[i - 1]
            prefix_b += count_b[i - 1]
            # Condition 1: all a < all b => a chars must be < i, b chars must be >= i
            res = min(res, (la - prefix_a) + prefix_b)
            # Condition 2: all b < all a
            res = min(res, (lb - prefix_b) + prefix_a)
        return res

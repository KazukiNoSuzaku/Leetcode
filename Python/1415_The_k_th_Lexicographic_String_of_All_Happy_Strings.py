# Author: Kaustav Ghosh
# Problem: The k-th Lexicographic String of All Happy Strings of Length n
# Approach: Generate happy strings or use math to find k-th directly

class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Total happy strings of length n: 3 * 2^(n-1)
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        k -= 1  # 0-indexed
        result = []
        # First char: 3 choices, each has 2^(n-1) strings
        group_size = 1 << (n - 1)
        first_idx = k // group_size
        result.append('abc'[first_idx])
        k %= group_size
        for i in range(1, n):
            group_size //= 2
            idx = k // group_size
            prev = result[-1]
            choices = [c for c in 'abc' if c != prev]
            result.append(choices[idx])
            k %= group_size
        return ''.join(result)

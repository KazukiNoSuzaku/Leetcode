# Author: Kaustav Ghosh
# Problem: 2167. Minimum Time to Remove All Cars Containing Illegal Goods
# URL: https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
# Difficulty: Hard

class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # left[i] = min cost to clear all illegal cars in s[0..i]
        # Options: remove from left end costs i+1
        #          or remove car at index i costs 2 (relative to prev)
        left = [0] * n
        left[0] = int(s[0]) * 1  # cost 1 to remove index 0 from left
        for i in range(1, n):
            if s[i] == '1':
                left[i] = min(left[i - 1] + 2, i + 1)
            else:
                left[i] = left[i - 1]

        # right[i] = min cost to clear all illegal cars in s[i..n-1]
        right = [0] * n
        right[n - 1] = int(s[n - 1]) * 1
        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                right[i] = min(right[i + 1] + 2, n - i)
            else:
                right[i] = right[i + 1]

        ans = min(left[n - 1], right[0])
        for i in range(n - 1):
            ans = min(ans, left[i] + right[i + 1])
        return ans

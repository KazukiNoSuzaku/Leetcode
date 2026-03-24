# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-good-numbers/

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        even_pos = (n + 1) // 2  # even indices: 0, 2, 4, ... -> 5 choices (0,2,4,6,8)
        odd_pos = n // 2          # odd indices: 1, 3, 5, ... -> 4 choices (2,3,5,7)
        return pow(5, even_pos, MOD) * pow(4, odd_pos, MOD) % MOD

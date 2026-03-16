# Author: Kaustav Ghosh
# Problem: Number of Ways to Paint N x 3 Grid
# Approach: DP counting 3-color (ABC) and 2-color (ABA) patterns per row

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # two_color = ABA patterns (6 total), three_color = ABC patterns (6 total)
        two_color = 6
        three_color = 6
        for _ in range(n - 1):
            new_two = (3 * two_color + 2 * three_color) % MOD
            new_three = (2 * two_color + 2 * three_color) % MOD
            two_color, three_color = new_two, new_three
        return (two_color + three_color) % MOD

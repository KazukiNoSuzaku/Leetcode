# Author: Kaustav Ghosh
# Problem: Number of Ways to Rearrange Sticks With K Sticks Visible
# Approach: Think about where the longest stick goes. Placed at the far left it is visible and hides nothing behind it, leaving the remaining sticks to supply one fewer visible stick among themselves. Placed anywhere else it is hidden by the longest stick to its left, and there are n minus one slots for it, each leaving the same subproblem with one fewer stick and the same visible count. That gives a two-term recurrence, the unsigned Stirling numbers of the first kind, which is filled bottom-up on a single rolling row so the thousand by thousand table never has to be stored.

class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # ways[v] is the count for the sticks placed so far with v of them visible.
        ways = [0] * (k + 1)
        ways[0] = 1
        for sticks in range(1, n + 1):
            for visible in range(min(sticks, k), 0, -1):
                ways[visible] = (ways[visible - 1] + (sticks - 1) * ways[visible]) % MOD
            ways[0] = 0
        return ways[k]

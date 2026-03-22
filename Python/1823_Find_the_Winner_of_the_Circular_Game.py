# Author: Kaustav Ghosh

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Josephus problem
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1

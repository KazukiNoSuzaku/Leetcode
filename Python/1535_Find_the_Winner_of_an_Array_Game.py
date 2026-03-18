# Author: Kaustav Ghosh
# Problem: 1535 - Find the Winner of an Array Game
# Approach: Simulate, track consecutive wins; if k >= n return max

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(arr):
            return max(arr)

        current = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if current > arr[i]:
                wins += 1
            else:
                current = arr[i]
                wins = 1
            if wins == k:
                return current

        return current

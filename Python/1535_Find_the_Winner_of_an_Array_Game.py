# Author: Kaustav Ghosh
# Problem: Find the Winner of an Array Game
# Approach: Linear scan — track current winner and consecutive win count; once k wins reached or array exhausted return current

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        current = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if arr[i] > current:
                current = arr[i]
                wins = 1
            else:
                wins += 1
            if wins >= k:
                return current
        return current

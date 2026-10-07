# Author: Kaustav Ghosh
# Problem: Find the Winner of an Array Game
# Approach: Carry the current champion along the array, counting consecutive wins and replacing it whenever a larger value appears. Once the array maximum takes over it never loses, so one pass suffices even for a k far larger than the array

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        champion = arr[0]
        wins = 0
        for challenger in arr[1:]:
            if champion > challenger:
                wins += 1
            else:
                champion = challenger
                wins = 1
            if wins == k:
                return champion
        return champion

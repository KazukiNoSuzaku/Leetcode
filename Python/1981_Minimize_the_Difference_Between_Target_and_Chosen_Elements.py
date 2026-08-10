# Author: Kaustav Ghosh
# Problem: Minimize the Difference Between Target and Chosen Elements
# Approach: Track the set of sums reachable by choosing one element per row so far. Add each row's distinct values to every reachable sum. Finally take the reachable sum closest to target

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        reachable = {0}
        for row in mat:
            values = set(row)
            reachable = {s + v for s in reachable for v in values}
        return min(abs(s - target) for s in reachable)

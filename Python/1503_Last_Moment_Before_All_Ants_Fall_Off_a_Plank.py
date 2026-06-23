# Author: Kaustav Ghosh
# Problem: Last Moment Before All Ants Fall Off a Plank
# Approach: Collisions equal pass-through; answer is max of left positions and (n - right positions)

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        ans = 0
        for pos in left:
            ans = max(ans, pos)
        for pos in right:
            ans = max(ans, n - pos)
        return ans

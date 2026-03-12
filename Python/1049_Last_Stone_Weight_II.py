# Author: Kaustav Ghosh
# 1049. Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        target = total // 2
        dp = {0}
        for s in stones:
            dp = {x + s for x in dp} | dp
        return min(abs(total - 2 * x) for x in dp if x <= target)

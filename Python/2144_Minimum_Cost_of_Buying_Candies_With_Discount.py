# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                total += cost[i]
        return total

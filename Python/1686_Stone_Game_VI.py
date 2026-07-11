# Author: Kaustav Ghosh
# Problem: Stone Game VI
# Approach: Each stone's priority is the combined value both players place on it; picking greedily by that sum is optimal, so alternate down the sorted order

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        order = sorted(range(len(aliceValues)),
                       key=lambda i: aliceValues[i] + bobValues[i],
                       reverse=True)
        alice = bob = 0
        for turn, i in enumerate(order):
            if turn % 2 == 0:
                alice += aliceValues[i]
            else:
                bob += bobValues[i]
        return (alice > bob) - (alice < bob)

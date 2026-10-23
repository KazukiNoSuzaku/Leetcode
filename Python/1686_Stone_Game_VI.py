# Author: Kaustav Ghosh
# Problem: Stone Game VI
# Approach: Taking a stone is worth its own value to the taker and simultaneously denies the opponent theirs, so the real prize attached to a stone is the sum of the two valuations, and that single number orders the stones by how urgently each should be claimed. Sorting by that combined worth descending and alternating picks is therefore optimal, and each player's score counts only their own valuations of the stones they actually took. Comparing the two totals gives the result, with equality reported separately.

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        order = sorted(range(len(aliceValues)),
                       key=lambda i: aliceValues[i] + bobValues[i], reverse=True)
        alice = 0
        bob = 0
        for turn, i in enumerate(order):
            if turn % 2 == 0:
                alice += aliceValues[i]
            else:
                bob += bobValues[i]
        if alice > bob:
            return 1
        return 0 if alice == bob else -1

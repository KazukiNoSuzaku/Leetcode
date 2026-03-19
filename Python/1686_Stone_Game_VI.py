# Author: Kaustav Ghosh
# https://leetcode.com/problems/stone-game-vi/

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        n = len(aliceValues)
        combined = sorted(range(n), key=lambda i: aliceValues[i] + bobValues[i], reverse=True)
        alice_score = sum(aliceValues[i] for i in combined[::2])
        bob_score = sum(bobValues[i] for i in combined[1::2])
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        return 0

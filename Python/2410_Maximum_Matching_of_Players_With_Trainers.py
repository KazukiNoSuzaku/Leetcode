# Author: Kaustav Ghosh
# Problem: Maximum Matching of Players With Trainers
# Approach: Sort both lists and walk the trainers in order, giving each one the weakest unmatched player it can take. Spending the smallest capable trainer on the weakest remaining player never blocks a match that another pairing would have allowed

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players = sorted(players)
        matched = 0
        for capacity in sorted(trainers):
            if matched < len(players) and players[matched] <= capacity:
                matched += 1
        return matched

# Author: Kaustav Ghosh
# Problem: Rank Teams by Votes
# Approach: Multi-key sort by vote counts per position

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        n = len(votes[0])
        count = {}
        for c in votes[0]:
            count[c] = [0] * n
        for vote in votes:
            for i, c in enumerate(vote):
                count[c][i] += 1
        teams = list(votes[0])
        teams.sort(key=lambda c: ([-x for x in count[c]], c))
        return ''.join(teams)

# During the NBA playoffs, we always set the stronger team to play with the weaker team.
# Given n teams, output the final contest matches in the given format.

# Author: Kaustav Ghosh

class Solution(object):
    def findContestMatch(self, n):
        teams = [str(i) for i in range(1, n + 1)]
        while len(teams) > 1:
            teams = ['(%s,%s)' % (teams[i], teams[-(i+1)]) for i in range(len(teams) // 2)]
        return teams[0]

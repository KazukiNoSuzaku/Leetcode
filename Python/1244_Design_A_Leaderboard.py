# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Hashmap for scores, sort for top K

from collections import defaultdict

class Leaderboard(object):
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.scores[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        return sum(sorted(self.scores.values(), reverse=True)[:K])

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.scores[playerId] = 0

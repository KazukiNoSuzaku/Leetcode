# Author: Kaustav Ghosh
# Problem: Node With Highest Edge Score
# Approach: Each node i has exactly one outgoing edge, which adds i to the score of edges[i], so accumulate the scores in one pass and return the highest-scoring node, which index() resolves to the smallest such node on ties

class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        score = [0] * len(edges)
        for i, j in enumerate(edges):
            score[j] += i
        return score.index(max(score))

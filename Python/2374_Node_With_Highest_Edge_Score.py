class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        score = [0] * len(edges)
        for src, dst in enumerate(edges):
            score[dst] += src
        return score.index(max(score))

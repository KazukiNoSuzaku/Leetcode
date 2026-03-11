# You are given an integer array score of n athletes. Return their relative ranks.
# Top 3 get "Gold Medal", "Silver Medal", "Bronze Medal"; rest get their rank as string.

# Author: Kaustav Ghosh

class Solution(object):
    def findRelativeRanks(self, score):
        order = sorted(range(len(score)), key=lambda i: -score[i])
        res = [''] * len(score)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        for rank, idx in enumerate(order):
            res[idx] = medals[rank] if rank < 3 else str(rank + 1)
        return res

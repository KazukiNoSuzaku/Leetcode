# Score of a pair (i, j) is values[i] + values[j] + i - j.
# Return maximum score of any pair i < j.

# Author: Kaustav Ghosh

class Solution(object):
    def maxScoreSightseeingPair(self, values):
        res = best_i = 0
        for j in range(1, len(values)):
            res = max(res, best_i + values[j] - j)
            best_i = max(best_i, values[j] + j)
        return res

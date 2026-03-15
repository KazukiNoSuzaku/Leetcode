# Return the indices of the k weakest rows (fewest 1s, tie broken by index).

# Author: Kaustav Ghosh

class Solution(object):
    def kWeakestRows(self, mat, k):
        strength = [(sum(row), i) for i, row in enumerate(mat)]
        strength.sort()
        return [i for _, i in strength[:k]]

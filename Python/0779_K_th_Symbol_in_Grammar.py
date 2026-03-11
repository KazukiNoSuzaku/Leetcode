# Find the k-th symbol (0-indexed) in the n-th row of a grammar sequence.

# Author: Kaustav Ghosh

class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1: return 0
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if k % 2 == 1: return parent
        return 1 - parent

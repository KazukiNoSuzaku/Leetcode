# Count columns to delete so all remaining columns are sorted lexicographically.

# Author: Kaustav Ghosh

class Solution(object):
    def minDeletionSize(self, strs):
        return sum(any(strs[r][c] > strs[r+1][c] for r in range(len(strs)-1)) for c in range(len(strs[0])))

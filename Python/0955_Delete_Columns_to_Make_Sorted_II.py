# Given an array of strings strs, delete the minimum number of columns
# so that the remaining columns are lexicographically non-decreasing row by row.

# Author: Kaustav Ghosh

class Solution(object):
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        cut = 0
        settled = [False] * (n - 1)
        for j in range(m):
            tmp = list(settled)
            bad = False
            for i in range(n - 1):
                if not tmp[i] and strs[i][j] > strs[i+1][j]:
                    bad = True
                    break
            if bad:
                cut += 1
            else:
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        settled[i] = True
        return cut

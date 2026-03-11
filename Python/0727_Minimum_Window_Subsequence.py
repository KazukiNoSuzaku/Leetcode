# Find the minimum window in s1 that contains s2 as a subsequence.

# Author: Kaustav Ghosh

class Solution(object):
    def minWindow(self, s1, s2):
        m, n = len(s1), len(s2)
        best = ''
        i = 0
        while i < m:
            j = 0
            while i < m and j < n:
                if s1[i] == s2[j]: j += 1
                i += 1
            if j == n:
                end = i
                i -= 1
                j -= 1
                while j >= 0:
                    if s1[i] == s2[j]: j -= 1
                    i -= 1
                i += 1
                if not best or end - i < len(best):
                    best = s1[i:end]
                i += 1
        return best

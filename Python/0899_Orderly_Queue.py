# If k==1 only rotations; if k>=2 any permutation, so sort.

# Author: Kaustav Ghosh

class Solution(object):
    def orderlyQueue(self, s, k):
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))

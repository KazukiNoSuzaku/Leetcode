# Check if an integer array can be split into consecutive subsequences of length >= 3.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def isPossible(self, nums):
        count = Counter(nums)
        end = Counter()
        for n in nums:
            if count[n] == 0: continue
            if end[n] > 0:
                end[n] -= 1
                end[n+1] += 1
            elif count[n+1] > 0 and count[n+2] > 0:
                count[n+1] -= 1
                count[n+2] -= 1
                end[n+3] += 1
            else:
                return False
            count[n] -= 1
        return True

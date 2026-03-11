# In a size 2N array, N+1 unique elements with one element repeated N times.
# Return the repeated element.

# Author: Kaustav Ghosh

class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for n in nums:
            if n in seen: return n
            seen.add(n)

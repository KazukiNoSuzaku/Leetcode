# Return the number of non-empty subarrays with a sum divisible by k.

# Author: Kaustav Ghosh

class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = {0: 1}
        prefix = 0
        res = 0
        for n in nums:
            prefix = (prefix + n) % k
            res += count.get(prefix, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return res

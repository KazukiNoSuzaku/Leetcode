# Return the number of good subarrays with exactly k distinct integers.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def at_most(k):
            count = defaultdict(int)
            left = res = 0
            for right, n in enumerate(nums):
                count[n] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k - 1)

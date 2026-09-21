# Author: Kaustav Ghosh
# Problem: Find All Good Indices
# Approach: Precompute, for every position, the length of the non-increasing run ending there and the length of the non-decreasing run starting there. Index i is good when the run ending just before it and the run starting just after it are both at least k long

class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ending = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                ending[i] = ending[i - 1] + 1
        starting = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                starting[i] = starting[i + 1] + 1
        return [i for i in range(k, n - k) if ending[i - 1] >= k and starting[i + 1] >= k]

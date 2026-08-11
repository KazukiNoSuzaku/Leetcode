# Author: Kaustav Ghosh
# Problem: Count Special Quadruplets
# Approach: Sweep k from high to low, keeping a frequency map of candidate fourth values nums[l] for l > k. For each pair i < j < k, the needed nums[l] is nums[i]+nums[j]+nums[k]; add its count

from collections import Counter

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = Counter()
        count = 0
        for k in range(n - 2, 1, -1):
            freq[nums[k + 1]] += 1
            for i in range(k - 1):
                for j in range(i + 1, k):
                    count += freq[nums[i] + nums[j] + nums[k]]
        return count

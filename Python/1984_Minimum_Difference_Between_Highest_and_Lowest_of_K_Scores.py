# Author: Kaustav Ghosh
# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Approach: After sorting, the k closest scores are contiguous. Slide a window of size k and take the smallest max-minus-min

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

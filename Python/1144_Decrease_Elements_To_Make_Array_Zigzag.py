# Author: Kaustav Ghosh
# Try two strategies: make even-indexed or odd-indexed elements valleys

class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        results = [0, 0]
        for strategy in range(2):
            for i in range(strategy, n, 2):
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < n - 1 else float('inf')
                neighbor_min = min(left, right)
                if nums[i] >= neighbor_min:
                    results[strategy] += nums[i] - neighbor_min + 1
        return min(results)

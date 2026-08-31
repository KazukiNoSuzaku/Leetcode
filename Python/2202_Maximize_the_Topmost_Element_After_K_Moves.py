# Author: Kaustav Ghosh
# Problem: Maximize the Topmost Element After K Moves
# Approach: With a single element, an odd number of moves leaves the pile empty (-1), even keeps it. Otherwise, with at least two elements and k>=2 we can either remove k-1 elements and put the best of them back on top (max of the first k-1), or remove exactly k elements leaving nums[k] on top when k<n. k==1 forces removing the top, exposing nums[1]

class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        if k == 1:
            return nums[1]
        # k >= 2 and n >= 2
        best = max(nums[:k - 1])  # slice caps at n automatically
        if k < n:
            best = max(best, nums[k])
        return best

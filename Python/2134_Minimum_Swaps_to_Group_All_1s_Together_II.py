# Author: Kaustav Ghosh
# Problem: Minimum Swaps to Group All 1's Together II
# Approach: All ones will occupy some circular window whose length equals the total count of ones. The fewest swaps is that length minus the maximum number of ones already inside any such window, found by sliding a fixed-size window around the circular array

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = sum(nums)
        if k == 0 or k == n:
            return 0

        current = sum(nums[:k])
        best = current
        for i in range(k, n + k):
            current += nums[i % n]
            current -= nums[(i - k) % n]
            best = max(best, current)
        return k - best

# Author: Kaustav Ghosh
# Sliding window: exactly k odd = atMost(k) - atMost(k-1)

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            count = 0
            left = 0
            odds = 0
            for right in range(len(nums)):
                odds += nums[right] % 2
                while odds > k:
                    odds -= nums[left] % 2
                    left += 1
                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)

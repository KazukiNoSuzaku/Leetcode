# Author: Kaustav Ghosh
# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# Difficulty: Easy
#
# Approach: First deduplicate consecutive equal elements (they form flat regions
# and the middle ones don't matter for hill/valley detection). Then scan the
# deduplicated array and count indices i (1 <= i <= len-2) where:
#   - arr[i] > arr[i-1] and arr[i] > arr[i+1]  (hill)
#   - arr[i] < arr[i-1] and arr[i] < arr[i+1]  (valley)

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Deduplicate consecutive equal values
        deduped = [nums[0]]
        for x in nums[1:]:
            if x != deduped[-1]:
                deduped.append(x)

        count = 0
        for i in range(1, len(deduped) - 1):
            if deduped[i] > deduped[i - 1] and deduped[i] > deduped[i + 1]:
                count += 1  # hill
            elif deduped[i] < deduped[i - 1] and deduped[i] < deduped[i + 1]:
                count += 1  # valley

        return count

# Author: Kaustav Ghosh
# Problem 1995: Count Special Quadruplets

from collections import Counter

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        # Use hash map: nums[d] - nums[c] == nums[a] + nums[b]
        # Iterate b from right to left
        right = Counter()
        for b in range(n - 2, 0, -1):
            # Add all (nums[d] - nums[b+1]) for d > b+1 when c = b+1
            c = b + 1
            for d in range(c + 1, n):
                right[nums[d] - nums[c]] += 1
            # Count pairs (a, b) where nums[a] + nums[b] exists in right
            for a in range(b):
                count += right.get(nums[a] + nums[b], 0)
        return count

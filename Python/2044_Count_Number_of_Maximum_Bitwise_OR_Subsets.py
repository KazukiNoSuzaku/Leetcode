# Author: Kaustav Ghosh
# Problem: Count Number of Maximum Bitwise-OR Subsets
# Approach: The maximum possible OR is the OR of all elements. Enumerate every subset (n is small) and count those whose OR equals that maximum

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 0
        for v in nums:
            target |= v

        n = len(nums)
        count = 0
        for mask in range(1, 1 << n):
            cur = 0
            for i in range(n):
                if mask >> i & 1:
                    cur |= nums[i]
            if cur == target:
                count += 1
        return count

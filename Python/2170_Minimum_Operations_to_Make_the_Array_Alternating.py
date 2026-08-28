# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make the Array Alternating
# Approach: All even indices must share one value and all odd indices another distinct value. Keep the most frequent value on each parity; if those top values collide, fall back to the better of (top even + runner-up odd) and (runner-up even + top odd). Changes are n minus the kept count

from collections import Counter

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def top_two(values):
            common = Counter(values).most_common(2)
            while len(common) < 2:
                common.append((None, 0))
            return common

        even = top_two(nums[0::2])
        odd = top_two(nums[1::2])

        if even[0][0] != odd[0][0]:
            keep = even[0][1] + odd[0][1]
        else:
            keep = max(even[0][1] + odd[1][1], even[1][1] + odd[0][1])
        return n - keep

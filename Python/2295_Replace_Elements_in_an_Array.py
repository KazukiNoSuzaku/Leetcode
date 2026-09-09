# Author: Kaustav Ghosh
# Problem: Replace Elements in an Array
# Approach: Values are unique, so keep a map from value to its index. Each operation replaces value a with b at that index and updates the map, giving O(1) per operation

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        pos = {v: i for i, v in enumerate(nums)}
        for a, b in operations:
            i = pos.pop(a)
            nums[i] = b
            pos[b] = i
        return nums

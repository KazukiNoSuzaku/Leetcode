# Author: Kaustav Ghosh
# Problem: Arithmetic Subarrays
# Approach: For each query slice, sort it and confirm every consecutive pair shares the same difference

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def is_arithmetic(sub):
            sub.sort()
            diff = sub[1] - sub[0]
            return all(sub[i] - sub[i - 1] == diff for i in range(2, len(sub)))

        return [is_arithmetic(nums[l[i]:r[i] + 1]) for i in range(len(l))]

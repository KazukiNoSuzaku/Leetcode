# Author: Kaustav Ghosh
# https://leetcode.com/problems/arithmetic-subarrays/

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for i in range(len(l)):
            sub = sorted(nums[l[i]:r[i] + 1])
            if len(sub) <= 2:
                result.append(True)
                continue
            diff = sub[1] - sub[0]
            is_arith = all(sub[j] - sub[j - 1] == diff for j in range(2, len(sub)))
            result.append(is_arith)
        return result

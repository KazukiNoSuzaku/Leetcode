# Author: Kaustav Ghosh

class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        idx = 0
        for group in groups:
            found = False
            while idx + len(group) <= len(nums):
                if nums[idx:idx + len(group)] == group:
                    idx += len(group)
                    found = True
                    break
                idx += 1
            if not found:
                return False
        return True

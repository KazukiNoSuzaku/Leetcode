# Author: Kaustav Ghosh
# Problem: All Divisions With the Highest Score of a Binary Array
# Approach: The score at a division is zeros to the left plus ones to the right. Sweep the split point maintaining left zeros and right ones incrementally, tracking the maximum score and every index achieving it

class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ones_right = sum(nums)
        zeros_left = 0
        best = ones_right          # score at index 0
        result = [0]
        for i, v in enumerate(nums):
            if v == 0:
                zeros_left += 1
            else:
                ones_right -= 1
            score = zeros_left + ones_right
            if score > best:
                best = score
                result = [i + 1]
            elif score == best:
                result.append(i + 1)
        return result

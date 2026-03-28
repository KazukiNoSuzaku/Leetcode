# Author: Kaustav Ghosh
# Problem: 2155. All Divisions With the Highest Score of a Binary Array
# URL: https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
# Approach: Prefix zeros count + suffix ones count, find indices with max score

class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total_ones = sum(nums)
        left_zeros = 0
        right_ones = total_ones
        max_score = 0
        result = []

        for i in range(n + 1):
            score = left_zeros + right_ones
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return result

# Author: Kaustav Ghosh
# Problem: Sum of Absolute Differences in a Sorted Array
# Approach: Because the array is already sorted, the absolute values can be dropped: every earlier element is at most the current one and every later element is at least, so the total splits into the current value times the count on each side, minus the sum of the smaller side and plus the sum of the larger. A single prefix total therefore answers each index in constant time, turning the quadratic pairwise sum into one pass.

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(nums)
        before = 0
        answer = []
        for i, value in enumerate(nums):
            after = total - before - value
            answer.append(i * value - before + after - (n - 1 - i) * value)
            before += value
        return answer

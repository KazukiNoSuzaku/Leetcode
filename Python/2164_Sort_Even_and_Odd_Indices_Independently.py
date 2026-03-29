# Author: Kaustav Ghosh
# Problem: 2164. Sort Even and Odd Indices Independently
# URL: https://leetcode.com/problems/sort-even-and-odd-indices-independently/
# Difficulty: Easy

class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)
        result = []
        i, j = 0, 0
        for k in range(len(nums)):
            if k % 2 == 0:
                result.append(evens[i])
                i += 1
            else:
                result.append(odds[j])
                j += 1
        return result

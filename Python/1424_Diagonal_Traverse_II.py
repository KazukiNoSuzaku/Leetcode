# Author: Kaustav Ghosh
# Problem: Diagonal Traverse II
# Approach: Group elements by i+j diagonal index

from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        diags = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i + j].append(nums[i][j])
        result = []
        for d in sorted(diags.keys()):
            result.extend(reversed(diags[d]))
        return result

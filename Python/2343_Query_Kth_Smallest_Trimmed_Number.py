# Author: Kaustav Ghosh
# Problem: Query Kth Smallest Trimmed Number
# Approach: All numbers have the same length, so trimmed values compare correctly as strings. For each distinct trim, sort the indices once by their last trim digits; the sort is stable, so equal trimmed values stay in index order as required. Each query then reads position k - 1 of the ordering for its trim

class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        orders = {}
        ans = []
        for k, trim in queries:
            if trim not in orders:
                orders[trim] = sorted(range(len(nums)), key=lambda i: nums[i][-trim:])
            ans.append(orders[trim][k - 1])
        return ans

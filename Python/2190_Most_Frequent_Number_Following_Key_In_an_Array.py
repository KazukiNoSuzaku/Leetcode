# Author: Kaustav Ghosh
# 2190. Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
# Difficulty: Easy
#
# Approach: Scan through nums. Whenever nums[i] == key and i+1 is valid,
# count nums[i+1] in a frequency map. Return the key with the highest count.
# Time: O(n), Space: O(n)

from collections import defaultdict

class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        count = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                count[nums[i + 1]] += 1
        return max(count, key=count.get)

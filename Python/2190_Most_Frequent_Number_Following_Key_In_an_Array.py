# Author: Kaustav Ghosh
# Problem: Most Frequent Number Following Key In an Array
# Approach: Scan adjacent pairs; whenever an element equals key, tally the element right after it. Return the tallied value with the highest count

from collections import Counter


class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        counts = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1
        return counts.most_common(1)[0][0]

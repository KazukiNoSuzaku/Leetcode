# Author: Kaustav Ghosh
# Problem: Distinct Numbers in Each Subarray (Premium)
# Approach: Slide a window of size k with a running counter; each step add the entering value, drop the leaving one, and the counter's size is the distinct count

from collections import Counter

class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums[:k])
        res = [len(counts)]
        for i in range(k, len(nums)):
            counts[nums[i]] += 1
            leaving = nums[i - k]
            counts[leaving] -= 1
            if counts[leaving] == 0:
                del counts[leaving]
            res.append(len(counts))
        return res

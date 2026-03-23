# Author: Kaustav Ghosh
# Problem 1852: Distinct Numbers in Each Subarray (Premium)

class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        count = defaultdict(int)
        result = []
        for i in range(len(nums)):
            count[nums[i]] += 1
            if i >= k:
                count[nums[i - k]] -= 1
                if count[nums[i - k]] == 0:
                    del count[nums[i - k]]
            if i >= k - 1:
                result.append(len(count))
        return result

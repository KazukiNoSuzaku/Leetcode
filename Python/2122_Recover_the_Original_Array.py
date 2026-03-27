# Author: Kaustav Ghosh
# https://leetcode.com/problems/recover-the-original-array/

from collections import Counter

class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            diff = nums[i] - nums[0]
            if diff == 0 or diff % 2 != 0:
                continue
            k = diff // 2
            count = Counter(nums)
            result = []
            valid = True
            for x in nums:
                if count[x] == 0:
                    continue
                if count[x + 2 * k] == 0:
                    valid = False
                    break
                result.append(x + k)
                count[x] -= 1
                count[x + 2 * k] -= 1
            if valid and len(result) == n // 2:
                return result

        return []

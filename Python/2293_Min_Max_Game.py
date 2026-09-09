# Author: Kaustav Ghosh
# Problem: Min Max Game
# Approach: Repeatedly halve the array: each new element is the min of its pair at even indices and the max at odd indices, until a single value remains

class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            nxt = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    nxt.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    nxt.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = nxt
        return nums[0]

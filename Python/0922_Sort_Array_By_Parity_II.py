# Arrange array so even-indexed positions have even numbers.

# Author: Kaustav Ghosh

class Solution(object):
    def sortArrayByParityII(self, nums):
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1: j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums

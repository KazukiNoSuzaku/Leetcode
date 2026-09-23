# Author: Kaustav Ghosh
# Problem: Merge Operations to Turn Array Into a Palindrome
# Approach: Compare the two ends. Equal ends are settled and both pointers move inward; otherwise the smaller end can only ever grow, so merging it with its neighbour is forced and costs one operation. Repeating that until the pointers meet counts the minimum

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        left, right = nums[i], nums[j]
        operations = 0
        while i < j:
            if left == right:
                i += 1
                j -= 1
                if i < j:
                    left, right = nums[i], nums[j]
            elif left < right:
                i += 1
                left += nums[i]
                operations += 1
            else:
                j -= 1
                right += nums[j]
                operations += 1
        return operations

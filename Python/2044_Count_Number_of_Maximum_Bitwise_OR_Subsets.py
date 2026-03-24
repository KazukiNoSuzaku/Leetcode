# Author: Kaustav Ghosh
# Problem 2044: Count Number of Maximum Bitwise-OR Subsets

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num
        count = [0]

        def backtrack(idx, curr_or):
            if idx == len(nums):
                if curr_or == max_or:
                    count[0] += 1
                return
            # Include nums[idx]
            backtrack(idx + 1, curr_or | nums[idx])
            # Exclude nums[idx]
            backtrack(idx + 1, curr_or)

        backtrack(0, 0)
        return count[0]

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array.
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1

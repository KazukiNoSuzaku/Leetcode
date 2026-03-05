# Given an unsorted array of integers nums, return the length of the longest consecutive
# elements sequence. You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,1,6,0,4]
# Output: 9

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0
        for n in num_set:
            if n - 1 not in num_set:
                curr = n
                length = 1
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                best = max(best, length)
        return best

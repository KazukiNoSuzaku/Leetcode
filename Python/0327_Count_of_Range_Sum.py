# Given an integer array nums and two integers lower and upper, return the number of range sums
# that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j
# inclusive, where i <= j.

# Example 1:
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] with sums -2, -1, and 2.

# Example 2:
# Input: nums = [0], lower = 0, upper = 0
# Output: 1

# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        def merge_count(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, lc = merge_count(arr[:mid])
            right, rc = merge_count(arr[mid:])
            count = lc + rc
            j = k = 0
            for val in left:
                while j < len(right) and right[j] - val < lower:
                    j += 1
                while k < len(right) and right[k] - val <= upper:
                    k += 1
                count += k - j
            return sorted(left + right), count

        _, total = merge_count(prefix)
        return total

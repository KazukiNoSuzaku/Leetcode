# Given an integer array nums, return an integer array counts where counts[i] is the number
# of smaller elements to the right of nums[i].

# Example 1:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]

# Example 2:
# Input: nums = [-1]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def countSmaller(self, nums):
        res = []
        sorted_list = []

        def bisect_left(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for n in reversed(nums):
            pos = bisect_left(sorted_list, n)
            res.append(pos)
            sorted_list.insert(pos, n)
        return res[::-1]

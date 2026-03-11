# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

# Author: Kaustav Ghosh

class Solution(object):
    def reversePairs(self, nums):
        self.count = 0

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            j = 0
            for val in left:
                while j < len(right) and val > 2 * right[j]:
                    j += 1
                self.count += j
            return sorted(left + right)

        merge_sort(nums)
        return self.count

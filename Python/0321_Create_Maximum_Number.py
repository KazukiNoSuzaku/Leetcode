# You are given two integer arrays nums1 and nums2 of lengths m and n respectively.
# nums1 and nums2 represent the digits of two numbers. You are also given an integer k.
# Create the maximum number of length k <= m + n from digits of the two numbers.
# The relative order of the digits from the same array must be preserved.
# Return an array of the k digits representing the answer.

# Example 1:
# Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# Output: [9,8,6,5,3]

# Example 2:
# Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
# Output: [6,7,6,0,4]

# Constraints:
# m == nums1.length, n == nums2.length
# 1 <= m, n <= 500
# 0 <= nums1[i], nums2[i] <= 9
# 1 <= k <= m + n

# Author: Kaustav Ghosh

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def max_subseq(nums, n):
            drop = len(nums) - n
            stack = []
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:n]

        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if a[i:] >= b[j:]:
                    res.append(a[i]); i += 1
                else:
                    res.append(b[j]); j += 1
            return res

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            s1 = max_subseq(nums1, i)
            s2 = max_subseq(nums2, k - i)
            candidate = merge(s1, s2)
            if candidate > best:
                best = candidate
        return best

# The next greater element of some element x in an array is the first greater element that
# is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each element in nums1, find the next greater element in nums2.

# Author: Kaustav Ghosh

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}
        for n in nums2:
            while stack and stack[-1] < n:
                nge[stack.pop()] = n
            stack.append(n)
        return [nge.get(n, -1) for n in nums1]

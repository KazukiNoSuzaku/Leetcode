# Given two lists that are anagrams, return mapping from A indices to B indices.

# Author: Kaustav Ghosh

class Solution(object):
    def anagramMappings(self, nums1, nums2):
        lookup = {v: i for i, v in enumerate(nums2)}
        return [lookup[n] for n in nums1]

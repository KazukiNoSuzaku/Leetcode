# Author: Kaustav Ghosh
# Problem: Two Out of Three
# Approach: Repeats inside a single array are irrelevant, since the question only asks whether a value appears in an array at all, so each array collapses to the set of its distinct values. A value then qualifies when it belongs to at least two of those three sets, which is settled by counting its memberships. Taking the union of the three sets gives every candidate exactly once, so each is tested once and the output carries no duplicates regardless of how often a value repeats in the inputs.

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        groups = [set(nums1), set(nums2), set(nums3)]
        answer = []
        for value in groups[0] | groups[1] | groups[2]:
            if sum(1 for group in groups if value in group) >= 2:
                answer.append(value)
        return answer

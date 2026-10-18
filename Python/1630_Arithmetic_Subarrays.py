# Author: Kaustav Ghosh
# Problem: Arithmetic Subarrays
# Approach: A set of numbers can be rearranged into an arithmetic sequence exactly when, sorted, its consecutive gaps are all equal, so each query is answered by sorting its own slice and comparing differences. Sorting is the honest cost here: the alternative of deriving the gap from the minimum, maximum and count and then checking membership needs the values to be distinct, which the problem never promises, and a slice such as three equal numbers would be mishandled by it.

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answers = []
        for start, end in zip(l, r):
            window = sorted(nums[start:end + 1])
            gap = window[1] - window[0]
            answers.append(all(window[i + 1] - window[i] == gap
                               for i in range(1, len(window) - 1)))
        return answers

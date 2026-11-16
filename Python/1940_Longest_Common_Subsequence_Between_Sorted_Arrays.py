# Author: Kaustav Ghosh
# Problem: Longest Common Subsequence Between Sorted Arrays
# Approach: Each array is strictly increasing, so it holds every one of its values at most once and in sorted order; that means any set of values present in all the arrays already appears in the same relative order in each of them and is automatically a common subsequence, and no common subsequence can contain a value some array lacks. The answer is therefore exactly the values common to every array, listed in increasing order, which I get by counting how many arrays each value occurs in and keeping those counted as often as there are arrays. Values are bounded by 100, so a fixed tally array gives this in time linear in the total input size.

class Solution(object):
    def longestCommonSubsequence(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: List[int]
        """
        holders = [0] * 101
        for array in arrays:
            for value in array:
                holders[value] += 1
        wanted = len(arrays)
        return [value for value in range(1, 101) if holders[value] == wanted]

# Author: Kaustav Ghosh
# Problem: Count Nice Pairs in an Array
# Approach: Rearranging the condition moves each index's own terms to its own side: nums[i] plus the reverse of nums[j] equalling nums[j] plus the reverse of nums[i] is the same as nums[i] minus its reverse equalling nums[j] minus its reverse. That value is a property of a single number, so the pairing collapses into grouping the numbers by it, and a group of size c supplies c choose 2 pairs. The reverse is taken by reversing the decimal string, which also disposes of the trailing zeros becoming leading ones.

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        MOD = 10 ** 9 + 7
        signatures = Counter(value - int(str(value)[::-1]) for value in nums)
        return sum(c * (c - 1) // 2 for c in signatures.values()) % MOD

# Author: Kaustav Ghosh
# Problem: Maximum Alternating Subarray Sum
# Approach: An alternating subarray always starts with a plus term. Track the best subarray ending at i where the current element is added (plus) or subtracted (minus). A plus can start fresh or extend a minus-ending run; a minus can only extend a plus-ending run

class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG = float('-inf')
        end_plus = NEG   # best alternating sum of subarray ending at i, i added
        end_minus = NEG  # ... i subtracted
        best = NEG
        for v in nums:
            new_plus = max(v, end_minus + v)
            new_minus = end_plus - v
            end_plus, end_minus = new_plus, new_minus
            best = max(best, end_plus, end_minus)
        return best

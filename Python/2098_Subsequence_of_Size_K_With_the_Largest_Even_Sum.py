# Author: Kaustav Ghosh
# Problem: Subsequence of Size K With the Largest Even Sum
# Approach: Take the k largest values. If their sum is even we are done. Otherwise flip parity with the smallest-loss swap: replace the smallest chosen odd with the largest unchosen even, or the smallest chosen even with the largest unchosen odd. Pick whichever keeps the sum largest; -1 if neither works

class Solution(object):
    def largestEvenSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        chosen = nums[:k]
        rest = nums[k:]
        total = sum(chosen)
        if total % 2 == 0:
            return total

        smallest_odd_in = next((x for x in reversed(chosen) if x % 2 == 1), None)
        smallest_even_in = next((x for x in reversed(chosen) if x % 2 == 0), None)
        largest_even_out = next((x for x in rest if x % 2 == 0), None)
        largest_odd_out = next((x for x in rest if x % 2 == 1), None)

        best = -1
        if smallest_odd_in is not None and largest_even_out is not None:
            best = max(best, total - smallest_odd_in + largest_even_out)
        if smallest_even_in is not None and largest_odd_out is not None:
            best = max(best, total - smallest_even_in + largest_odd_out)
        return best

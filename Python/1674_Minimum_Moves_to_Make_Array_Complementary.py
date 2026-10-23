# Author: Kaustav Ghosh
# Problem: Minimum Moves to Make Array Complementary
# Approach: Every pair of mirrored elements must end up at the same common total, and each pair's cost depends only on that total, so the plan is to work out the cost of every candidate total from 2 to twice the limit and take the cheapest. For a pair, the total it already has is free; changing one element reaches any total from one above the smaller element up to the limit plus the larger one; anything outside that needs both changed. Writing those three verdicts as a range of two, a range of one, and a single point of zero lets each pair be recorded in constant time on a difference array, so the whole sweep costs the length of the array plus the span of totals rather than their product.

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        top = 2 * limit
        delta = [0] * (top + 2)
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            low, high = (a, b) if a < b else (b, a)
            # Two moves everywhere by default.
            delta[2] += 2
            delta[top + 1] -= 2
            # One move suffices across this span.
            delta[low + 1] -= 1
            delta[high + limit + 1] += 1
            # And the total they already make is free.
            delta[a + b] -= 1
            delta[a + b + 1] += 1

        best = None
        running = 0
        for total in range(2, top + 1):
            running += delta[total]
            if best is None or running < best:
                best = running
        return best

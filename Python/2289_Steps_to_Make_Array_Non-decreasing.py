# Author: Kaustav Ghosh
# Problem: Steps to Make Array Non-decreasing
# Approach: Each element is eventually removed by the nearest larger element on its left. Sweep right to left with a decreasing stack; a value "eats" all smaller values to its right, and the step at which it finishes is one more than the current chain, but never less than the steps a swallowed element already required. The answer is the maximum removal step over all elements

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []  # (value, steps_needed_to_remove_this_element)
        ans = 0
        for x in reversed(nums):
            cur = 0
            while stack and stack[-1][0] < x:
                cur = max(cur + 1, stack.pop()[1])
            stack.append((x, cur))
            ans = max(ans, cur)
        return ans

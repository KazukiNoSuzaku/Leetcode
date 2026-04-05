# Author: Kaustav Ghosh
# 2202. Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
# Difficulty: Medium
#
# Approach: Case analysis:
#   - If n==1 and k is odd -> impossible, return -1 (only one element, always pushed back).
#   - If k==0 -> return nums[0].
#   - If k==1 -> stack must have >=2 elements to expose nums[1], else -1.
#   - Otherwise (k>=2):
#       Best is either the max among the first k elements (remove top k times)
#       or nums[k] if it exists (skip top k elements by removing k-1 then push k-th).
#       Specifically: candidate = max of nums[0..min(k-1, n-1)],
#       then also consider nums[k] if k < n.

class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Edge: single element - after odd moves we have empty stack
        if n == 1:
            if k % 2 == 1:
                return -1
            return nums[0]

        if k == 0:
            return nums[0]

        # We can remove up to k elements from the top (one per move) and push one back.
        # After k moves, the top can be:
        #   max(nums[0..k-2]) by removing first k elements then pushing nums[k-1] back
        #   But we want to maximise, so best from first k-1 elements (push one back)
        #   OR nums[k] itself sitting at top after removing exactly k elements.

        # Candidates: any of nums[0..k-2] (we remove k-1, push that back), and nums[k]
        res = -1

        # Consider nums[k] if reachable (remove exactly k elements)
        if k < n:
            res = max(res, nums[k])

        # Consider any of the first min(k-1, n) elements (remove k-1, push chosen back)
        for i in range(min(k - 1, n)):
            res = max(res, nums[i])

        return res

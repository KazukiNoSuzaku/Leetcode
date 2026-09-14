# Author: Kaustav Ghosh
# Problem: Max Sum of a Pair With Equal Sum of Digits
# Approach: Scan once, remembering only the largest number seen so far for each digit sum. A new number pairs best with that largest earlier number, so update the answer with their sum before updating the stored maximum

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = {}
        ans = -1
        for x in nums:
            s = sum(int(d) for d in str(x))
            if s in best:
                ans = max(ans, best[s] + x)
                best[s] = max(best[s], x)
            else:
                best[s] = x
        return ans

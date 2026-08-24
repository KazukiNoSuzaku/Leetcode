# Author: Kaustav Ghosh
# Problem: Elements in Array After Removing and Replacing Elements
# Approach: The array cycles with period 2n: for the first n minutes it shrinks from the front (nums[t:]), then regrows from the start (nums[:t-n]). For each query reduce time mod 2n and index into the appropriate phase, returning -1 when the index is out of the current length

class Solution(object):
    def elementInNums(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        period = 2 * n
        result = []
        for time, index in queries:
            t = time % period
            if t <= n:
                # array is nums[t:], length n-t
                if index < n - t:
                    result.append(nums[t + index])
                else:
                    result.append(-1)
            else:
                # array is nums[:t-n], length t-n
                if index < t - n:
                    result.append(nums[index])
                else:
                    result.append(-1)
        return result

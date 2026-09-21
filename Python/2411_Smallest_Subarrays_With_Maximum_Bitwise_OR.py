# Author: Kaustav Ghosh
# Problem: Smallest Subarrays With Maximum Bitwise OR
# Approach: Extending a subarray only ever adds bits, so the maximum OR starting at i is the OR of the whole suffix. Scanning right to left, remember for each bit the nearest index where it is set; the subarray must stretch to the farthest of those, so the answer is max(1, farthest - i + 1)

class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        last = [0] * 30
        answer = [1] * n
        for i in range(n - 1, -1, -1):
            for bit in range(30):
                if nums[i] >> bit & 1:
                    last[bit] = i
            answer[i] = max(1, max(last) - i + 1)
        return answer

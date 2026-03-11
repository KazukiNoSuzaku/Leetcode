# In a binary array, a k-bit flip reverses k consecutive bits.
# Return the minimum number of flips to make all bits 1, or -1 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flipped = [0] * n
        flips = res = 0
        for i in range(n):
            if i >= k:
                flips ^= flipped[i - k]
            if nums[i] ^ flips == 0:
                if i + k > n: return -1
                flipped[i] = 1
                flips ^= 1
                res += 1
        return res

class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        # OR of a subset equals 2^k only if 2^k is in nums; find smallest missing power of 2.
        nums_set = set(nums)
        x = 1
        while x in nums_set:
            x <<= 1
        return x

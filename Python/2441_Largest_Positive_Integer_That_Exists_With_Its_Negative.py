class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        s = set(nums)
        return max((x for x in nums if x > 0 and -x in s), default=-1)

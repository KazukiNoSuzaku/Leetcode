class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        return i + (n - 1 - j) - (1 if i > j else 0)

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return [int(d) for n in nums for d in str(n)]

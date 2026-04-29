class Solution:
    def averageValue(self, nums: list[int]) -> int:
        vals = [x for x in nums if x % 6 == 0]
        return sum(vals) // len(vals) if vals else 0

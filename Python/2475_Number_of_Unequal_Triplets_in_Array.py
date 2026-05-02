from collections import Counter

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        # For each distinct middle value, count left elements (different values before it)
        # and right elements (different values after it).
        count = Counter(nums)
        ans = 0
        left = 0
        for c in count.values():
            right = len(nums) - left - c
            ans += left * c * right
            left += c
        return ans

class Solution:
    def subsequenceSumOr(self, nums: list[int]) -> int:
        # Premium: OR each element and each running prefix sum.
        # Prefix sums capture carry-propagated bits not visible in individual elements.
        ans = 0
        running = 0
        for x in nums:
            ans |= x
            running += x
            ans |= running
        return ans

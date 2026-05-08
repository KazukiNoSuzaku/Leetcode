class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        # Element sum ≥ digit sum always (each number ≥ its digit sum), so abs is redundant but harmless.
        element_sum = sum(nums)
        digit_sum = sum(int(d) for n in nums for d in str(n))
        return abs(element_sum - digit_sum)

class Solution:
    def numberOfEvenSubarrays(self, nums: list[int]) -> int:
        # Premium: even product iff at least one even element.
        # Count all-odd subarrays: from last even element +1 to current index.
        n = len(nums)
        total = n * (n + 1) // 2
        odd_count = 0
        last_even = -1
        for i, x in enumerate(nums):
            if x % 2 == 0:
                last_even = i
            odd_count += i - last_even  # all-odd subarrays ending at i
        return total - odd_count

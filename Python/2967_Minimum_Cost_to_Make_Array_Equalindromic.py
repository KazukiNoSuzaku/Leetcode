from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def is_palindrome(n: int) -> bool:
            s = str(n)
            return s == s[::-1]

        def cost(target: int) -> int:
            return sum(abs(x - target) for x in nums)

        nums.sort()
        med = nums[len(nums) // 2]

        # Search nearest palindrome at or above and at or below median
        best = float('inf')
        for start, direction in [(med, 1), (med, -1)]:
            n = start
            while True:
                if is_palindrome(n):
                    best = min(best, cost(n))
                    break
                n += direction
        return best

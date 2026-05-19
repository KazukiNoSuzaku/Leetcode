class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2: return False
            if x == 2: return True
            if x % 2 == 0: return False
            for d in range(3, int(x**0.5) + 1, 2):
                if x % d == 0: return False
            return True

        n = len(nums)
        ans = 0
        for i in range(n):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][n - 1 - i]):
                ans = max(ans, nums[i][n - 1 - i])
        return ans

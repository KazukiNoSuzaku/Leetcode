from typing import List

class Solution:
    def maxPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        prime_indices = [i for i, n in enumerate(nums) if is_prime(n)]
        return prime_indices[-1] - prime_indices[0]

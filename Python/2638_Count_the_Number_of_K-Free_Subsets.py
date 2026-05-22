class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 2 ** len(nums)

        num_set = set(nums)
        visited: set[int] = set()
        ans = 1

        for x in sorted(nums):
            if x in visited:
                continue
            chain_len = 0
            cur = x
            while cur in num_set:
                visited.add(cur)
                chain_len += 1
                cur += k
            # Non-adjacent subsets of a chain of length m = Fib(m+2)
            a, b = 1, 2
            for _ in range(chain_len):
                a, b = b, a + b
            ans *= a

        return ans

class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        best_div, best_score = -1, -1
        for d in sorted(divisors):
            score = sum(1 for n in nums if n % d == 0)
            if score > best_score:
                best_score = score
                best_div = d
        return best_div

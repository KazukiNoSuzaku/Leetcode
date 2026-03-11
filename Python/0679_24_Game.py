# Check if four numbers can be combined with +,-,*,/ and parentheses to equal 24.

# Author: Kaustav Ghosh

from itertools import permutations

class Solution(object):
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    for c in [a+b, a-b, a*b] + ([a/b] if b != 0 else []):
                        if solve(rest + [c]): return True
            return False
        return solve([float(x) for x in cards])

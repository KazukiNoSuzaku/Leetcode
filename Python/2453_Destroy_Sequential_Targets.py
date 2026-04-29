from collections import defaultdict

class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        # nums[i] destroys all nums[j] where nums[j] ≡ nums[i] (mod space)
        # Group by residue; pick the group with most members (tie-break: smallest seed)
        groups = defaultdict(list)
        for x in nums:
            groups[x % space].append(x)
        best_count, ans = 0, float('inf')
        for g in groups.values():
            mn = min(g)
            c = len(g)
            if c > best_count or (c == best_count and mn < ans):
                best_count, ans = c, mn
        return ans

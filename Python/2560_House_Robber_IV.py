class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        # Binary search on capability; greedy check: skip houses > cap, greedily rob eligible non-adjacent.
        def feasible(cap):
            count = i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    if count == k:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

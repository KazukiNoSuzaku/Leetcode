class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)

        def can_form(d: int) -> bool:
            count = i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= d:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_form(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

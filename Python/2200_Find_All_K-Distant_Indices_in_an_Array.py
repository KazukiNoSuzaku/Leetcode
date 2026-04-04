# Author: Kaustav Ghosh

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        # type: (List[int], int, int) -> List[int]
        n = len(nums)
        result = []
        last_added = -1  # Track last added index to avoid duplicates

        for j in range(n):
            if nums[j] == key:
                # All i where |i - j| <= k
                lo = max(0, j - k)
                hi = min(n - 1, j + k)
                start = max(lo, last_added + 1)
                for i in range(start, hi + 1):
                    result.append(i)
                if hi >= start:
                    last_added = hi

        return result

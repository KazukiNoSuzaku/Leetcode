from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0
        for i in range(n - m):
            match = True
            for j in range(m):
                diff = nums[i + j + 1] - nums[i + j]
                if pattern[j] == 1 and diff <= 0:
                    match = False; break
                if pattern[j] == 0 and diff != 0:
                    match = False; break
                if pattern[j] == -1 and diff >= 0:
                    match = False; break
            if match:
                count += 1
        return count

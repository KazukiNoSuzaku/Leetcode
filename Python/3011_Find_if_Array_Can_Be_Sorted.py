from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        prev_max = float('-inf')
        while i < n:
            j = i
            pc = bin(nums[i]).count('1')
            while j < n and bin(nums[j]).count('1') == pc:
                j += 1
            segment = sorted(nums[i:j])
            if segment[0] < prev_max:
                return False
            prev_max = segment[-1]
            i = j
        return True

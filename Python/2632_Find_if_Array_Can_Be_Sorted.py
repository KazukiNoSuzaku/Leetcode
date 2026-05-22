class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        prev_max = float('-inf')
        i, n = 0, len(nums)
        while i < n:
            j = i
            pc = bin(nums[i]).count('1')
            while j < n and bin(nums[j]).count('1') == pc:
                j += 1
            seg_min = min(nums[i:j])
            seg_max = max(nums[i:j])
            if seg_min < prev_max:
                return False
            prev_max = seg_max
            i = j
        return True

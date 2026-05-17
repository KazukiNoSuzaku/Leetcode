class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()
        ptr = 0
        for x in nums:
            if x > nums[ptr]:
                ptr += 1
        return ptr

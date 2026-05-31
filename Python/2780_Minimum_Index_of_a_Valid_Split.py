class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        candidate, count = nums[0], 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1

        total = nums.count(candidate)
        n = len(nums)
        left_count = 0
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            right_count = total - left_count
            if left_count * 2 > i + 1 and right_count * 2 > n - i - 1:
                return i
        return -1

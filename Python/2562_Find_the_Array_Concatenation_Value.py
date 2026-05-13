class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        # Two pointers: concatenate first and last as strings, add to value; middle singleton added directly.
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            ans += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            ans += nums[l]
        return ans

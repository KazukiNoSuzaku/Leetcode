# Premium problem
# Two pointers from both ends; merge the smaller side with its neighbor, counting operations.

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        left, right = nums[lo], nums[hi]
        ops = 0
        while lo < hi:
            if left == right:
                lo += 1
                hi -= 1
                if lo < hi:
                    left, right = nums[lo], nums[hi]
            elif left < right:
                lo += 1
                left += nums[lo]
                ops += 1
            else:
                hi -= 1
                right += nums[hi]
                ops += 1
        return ops

class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        # Sort; optimally pair the first n//2 elements with the second half using two pointers.
        nums.sort()
        n = len(nums)
        j = n // 2
        count = 0
        for i in range(n // 2):
            while j < n and nums[j] < 2 * nums[i]:
                j += 1
            if j < n:
                count += 2
                j += 1
        return count

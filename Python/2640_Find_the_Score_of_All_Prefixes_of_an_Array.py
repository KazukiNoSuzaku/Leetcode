class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        running_max = running_sum = 0
        for i, x in enumerate(nums):
            running_max = max(running_max, x)
            running_sum += x + running_max
            ans[i] = running_sum
        return ans

class Solution:
    def maxSum(self, nums: list[int]) -> int:
        best = {}
        ans = -1
        for x in nums:
            d = max(int(c) for c in str(x))
            if d in best:
                ans = max(ans, best[d] + x)
            if d not in best or x > best[d]:
                best[d] = x
        return ans

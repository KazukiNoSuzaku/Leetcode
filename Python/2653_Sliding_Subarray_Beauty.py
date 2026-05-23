from collections import defaultdict

class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        freq = defaultdict(int)

        def xth_smallest():
            count = 0
            for v in range(-50, 0):
                count += freq[v]
                if count >= x:
                    return v
            return 0

        for i in range(k):
            if nums[i] < 0:
                freq[nums[i]] += 1

        ans = [xth_smallest()]
        for i in range(k, len(nums)):
            if nums[i] < 0:
                freq[nums[i]] += 1
            if nums[i - k] < 0:
                freq[nums[i - k]] -= 1
            ans.append(xth_smallest())
        return ans

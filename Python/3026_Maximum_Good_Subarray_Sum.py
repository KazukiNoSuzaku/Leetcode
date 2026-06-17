from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # A good subarray [i..j] satisfies |nums[i] - nums[j]| == k
        # For each j, find i with nums[i] in {nums[j]+k, nums[j]-k} minimising prefix[i]
        prefix = 0
        min_pre: dict[int, float] = {}  # value -> min prefix sum at an index with that value
        ans = float('-inf')

        for x in nums:
            for target in (x + k, x - k):
                if target in min_pre:
                    ans = max(ans, prefix + x - min_pre[target])
            # Record prefix before x so i < j (update after checking)
            if x not in min_pre or prefix < min_pre[x]:
                min_pre[x] = prefix
            prefix += x

        return ans if ans != float('-inf') else 0

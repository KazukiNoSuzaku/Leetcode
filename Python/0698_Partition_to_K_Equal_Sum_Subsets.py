# Determine if an array can be partitioned into k subsets with equal sum.

# Author: Kaustav Ghosh

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k: return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target: return False
        buckets = [0] * k
        def backtrack(idx):
            if idx == len(nums): return True
            seen = set()
            for i in range(k):
                if buckets[i] in seen: continue
                if buckets[i] + nums[idx] <= target:
                    seen.add(buckets[i])
                    buckets[i] += nums[idx]
                    if backtrack(idx + 1): return True
                    buckets[i] -= nums[idx]
            return False
        return backtrack(0)

# Find 3 non-overlapping subarrays of size k with maximum sum; return their starting indices.

# Author: Kaustav Ghosh

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        sums = [sum(nums[:k])]
        for i in range(k, n):
            sums.append(sums[-1] + nums[i] - nums[i-k])
        left = [0] * n
        best = sums[0]
        for i in range(1, n):
            if sums[i] > best:
                best = sums[i]
                left[i] = i
            else:
                left[i] = left[i-1]
        right = [0] * n
        best = sums[n-k]
        right[n-k] = n-k
        for i in range(n-k-1, -1, -1):
            if sums[i] >= best:
                best = sums[i]
                right[i] = i
            else:
                right[i] = right[i+1]
        res = None
        for mid in range(k, n-2*k+1):
            l, r = left[mid-k], right[mid+k]
            total = sums[l] + sums[mid] + sums[r]
            if res is None or total > sums[res[0]] + sums[res[1]] + sums[res[2]]:
                res = [l, mid, r]
        return res

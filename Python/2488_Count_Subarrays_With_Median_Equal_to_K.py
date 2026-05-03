from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # Median == k iff (#greater - #less) is 0 (odd length) or -1 (even length).
        # Transform: +1 for >k, -1 for <k, 0 for =k.
        # Subarray sum = prefix[r+1] - prefix[l]; want sum in {0, -1}.
        # For subarrays containing k_pos: count left prefixes matching prefix[r+1] or +1 above.
        k_pos = nums.index(k)
        pre = defaultdict(int)
        pre[0] = 1
        score = ans = 0

        for i, x in enumerate(nums):
            score += (1 if x > k else -1 if x < k else 0)
            if i >= k_pos:
                ans += pre[score] + pre[score + 1]
            else:
                pre[score] += 1

        return ans

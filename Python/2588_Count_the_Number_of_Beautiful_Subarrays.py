from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        # A subarray is beautiful if XOR of all elements == 0.
        # Count pairs of equal prefix XORs.
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0
        for x in nums:
            prefix ^= x
            ans += count[prefix]
            count[prefix] += 1
        return ans

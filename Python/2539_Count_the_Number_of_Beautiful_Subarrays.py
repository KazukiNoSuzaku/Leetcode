from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        # Subarray is beautiful iff XOR = 0; count pairs of equal prefix XORs via hashmap.
        count = defaultdict(int)
        count[0] = 1
        prefix = ans = 0
        for x in nums:
            prefix ^= x
            ans += count[prefix]
            count[prefix] += 1
        return ans

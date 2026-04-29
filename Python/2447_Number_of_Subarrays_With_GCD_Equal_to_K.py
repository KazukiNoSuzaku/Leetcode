from math import gcd

class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            g = 0
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == k:
                    ans += 1
                elif g < k:
                    break
        return ans

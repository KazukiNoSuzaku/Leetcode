from math import gcd

class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = lcm * nums[j] // gcd(lcm, nums[j])
                if lcm == k:
                    ans += 1
                elif lcm > k:
                    break
        return ans

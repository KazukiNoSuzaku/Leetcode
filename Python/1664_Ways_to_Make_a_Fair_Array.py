# Author: Kaustav Ghosh
# Problem: Ways to Make a Fair Array
# Approach: Removing index i flips the parity of everything after it; using even/odd suffix sums, a removal is fair when evenPrefix+oddSuffix == oddPrefix+evenSuffix

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        even_suf = [0] * (n + 1)
        odd_suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            even_suf[i] = even_suf[i + 1] + (nums[i] if i % 2 == 0 else 0)
            odd_suf[i] = odd_suf[i + 1] + (nums[i] if i % 2 == 1 else 0)

        count = 0
        even_pre = odd_pre = 0
        for i in range(n):
            new_even = even_pre + odd_suf[i + 1]
            new_odd = odd_pre + even_suf[i + 1]
            if new_even == new_odd:
                count += 1
            if i % 2 == 0:
                even_pre += nums[i]
            else:
                odd_pre += nums[i]
        return count

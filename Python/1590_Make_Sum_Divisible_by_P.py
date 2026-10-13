# Author: Kaustav Ghosh
# Problem: Make Sum Divisible by P
# Approach: Removing a block leaves the rest divisible by p exactly when the removed block's sum is congruent to the whole array's remainder, so the task becomes finding the shortest subarray with that remainder. Writing a subarray's sum as a difference of prefix sums, the condition fixes the remainder of the earlier prefix given the current one, so I keep the most recent index at which each prefix remainder appeared and look up the single remainder I need. Keeping the most recent one is what makes the subarray shortest. A remainder of zero needs no removal, and the whole array may never be removed.

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0

        last_seen = {0: -1}
        best = n
        running = 0
        for i, value in enumerate(nums):
            running = (running + value) % p
            wanted = (running - target) % p
            if wanted in last_seen:
                length = i - last_seen[wanted]
                if length < best:
                    best = length
            last_seen[running] = i
        return best if best < n else -1
